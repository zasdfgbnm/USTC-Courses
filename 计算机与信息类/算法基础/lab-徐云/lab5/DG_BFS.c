#include<stdio.h>
#include<map>
#include<vector>
using namespace std; 
map<int, vector<int> > g;

void readData(char *file)
{
    int a,b; 
    char c; 
    FILE *fp = fopen(file,'r');
    while(!eof(fp)){
        fscanf(fp,"%d",&a);
        fgetc(fp);
        fscanf(fp,"%d",&b);
        fgetc(fp);
        if(g.count(a)==0){
            g.insert(pair<int,vector<int> >(a,vector<int>(b)));
        }else{
            auto p = g.find(a);
            *p.push_back(b);
        }
    }
    fclose(fp);
}

void bfs()
{

