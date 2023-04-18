#include <omp.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

unsigned int seed =                         0;

int	         NowYear =                      2023;   // 2023 - 2028
int	         NowMonth =                     0;		// 0 (JAN) - 11 (DEC)

float	     NowPrecip;		                        // inches of rain per month
float	     NowTemp;		                        // temperature this month
float	     NowHeight =                    5;		// rye grass height in inches
int	         NowNumRabbits =                1;		// number of rabbits in the current population

const float RYEGRASS_GROWS_PER_MONTH =		20.0;
const float ONE_RABBITS_EATS_PER_MONTH =	1.0;

const float AVG_PRECIP_PER_MONTH =	        12.0;	// average
const float AMP_PRECIP_PER_MONTH =		    4.0;	// plus or minus
const float RANDOM_PRECIP =			        2.0;	// plus or minus noise

const float AVG_TEMP =				        60.0;	// average
const float AMP_TEMP =				        20.0;	// plus or minus
const float RANDOM_TEMP =			        10.0;	// plus or minus noise

const float MIDTEMP =				        60.0;
const float MIDPRECIP =				        14.0;

float
Ranf( unsigned int *seedp,  float low, float high )
{
        float r = (float) rand_r( seedp );              // 0 - RAND_MAX

        return( low  +  r * ( high - low ) / (float)RAND_MAX );
}

float
Sqr( float x )
{
        return x*x;
}

void
incrementDate ()
{
    NowMonth++;
        if( NowMonth == 12 )
        {
            NowYear++;
            NowMonth = 0;
        }
}

void getEnvironmentalVariables( float* tempFactor, float* precipFactor ) 
{
    float x = Ranf( &seed, -1.f, 1.f );

    float ang = ( 30.*(float)NowMonth + 15. ) * ( M_PI / 180. );

    float temp = AVG_TEMP - AMP_TEMP * cos( ang );
    NowTemp = temp + Ranf( &seed, -RANDOM_TEMP, RANDOM_TEMP );

    float precip = AVG_PRECIP_PER_MONTH + AMP_PRECIP_PER_MONTH * sin( ang );
    NowPrecip = precip + Ranf( &seed,  -RANDOM_PRECIP, RANDOM_PRECIP );
    if( NowPrecip < 0. ) NowPrecip = 0.;

    (*tempFactor) = exp( -Sqr((NowTemp - MIDTEMP) / 10. ));
    (*precipFactor) = exp( -Sqr((NowPrecip - MIDPRECIP) / 10. ));
}

int
Rabbits( )
{
    while( NowYear < 2029 )
    {
        int nextNumRabbits = NowNumRabbits;
        int carryingCapacity = (int)( NowHeight );

        if (nextNumRabbits < carryingCapacity) 
        {
            nextNumRabbits++;
        }
        else if (nextNumRabbits > carryingCapacity) 
        {
            nextNumRabbits--;
        }

        if( nextNumRabbits < 0 ) nextNumRabbits = 0;
        
        // DoneComputing barrier:
        #pragma omp barrier

        NowNumRabbits = nextNumRabbits;

        // DoneAssigning barrier:
        #pragma omp barrier

        // DonePrinting barrier:
        #pragma omp barrier
    }
}

int
RyeGrass( float* tempFactor, float* precipFactor )
{
    while( NowYear < 2029 )
    {
        float nextHeight = NowHeight;

        nextHeight += (*tempFactor) * (*precipFactor) * RYEGRASS_GROWS_PER_MONTH;
        nextHeight -= (float)NowNumRabbits * ONE_RABBITS_EATS_PER_MONTH;

        if( nextHeight < 0. ) nextHeight = 0.;

        // DoneComputing barrier:
        #pragma omp barrier

        NowHeight = nextHeight;

        // DoneAssigning barrier:
        #pragma omp barrier

        // DonePrinting barrier:
        #pragma omp barrier
    }
}

int
Watcher( float* tempFactor, float* precipFactor )
{
    while( NowYear < 2029 )
    {

        // DoneComputing barrier:
        #pragma omp barrier

        // DoneAssigning barrier:
        #pragma omp barrier

        fprintf(stderr, "YEAR: %d, MONTH: %d, Temp: %.2f, Precip: %.2f, GHeight: %.2f, Rabbit#: %d \n", 
                NowYear, NowMonth, NowTemp, NowPrecip, NowHeight, NowNumRabbits);

        incrementDate();

        getEnvironmentalVariables( tempFactor, precipFactor );

        // DonePrinting barrier:
        #pragma omp barrier
    }
}

int
MyAgent( )
{
    while( NowYear < 2029 )
    {

        // DoneComputing barrier:
        #pragma omp barrier

        // DoneAssigning barrier:
        #pragma omp barrier

        // DonePrinting barrier:
        #pragma omp barrier
    }
}

int main( ) 
{
#ifdef   _OPENMP
	//fprintf( stderr, "OpenMP version %d is supported here\n", _OPENMP );
#else
	fprintf( stderr, "OpenMP is not supported here - sorry!\n" );
	exit( 0 );
#endif   

    // initialize starting enviornmental variables
    float tempFactor;
    float precipFactor;
    
    getEnvironmentalVariables( &tempFactor, &precipFactor );

    omp_set_num_threads(4); // set number of threads
    #pragma omp parallel sections
    {
        #pragma omp section
        {
            Rabbits();
        }

        #pragma omp section
        {
            RyeGrass( &tempFactor, &precipFactor );
        }

        #pragma omp section
        {
            Watcher( &tempFactor, &precipFactor );
        }

        #pragma omp section
        {
            MyAgent();
        }
    } // implied barrier -- all functions must return in order
      // to allow any of them to get past here

    return 0;
}