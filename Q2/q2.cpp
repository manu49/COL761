#include<bits/stdc++.h>
#include<cstdlib>
#include "string"

//#include<ctime>
#include "cstring"
#include "sstream"

#include "iostream"
#include "vector"
#include<chrono>


using namespace std;


int main(int argc,char **argv){

   vector<int> dimensions = {2,4,8,10};
   int k = 1;

   vector<string> temp_storage = {"2","4","8","10"};

   for(int i= 0; i <= 3 ; i++){
      reduce_dimension(temp_storage[i] 3, 3, 0.90, dimensions[i],1,outfile);
   }

   return(0)
}