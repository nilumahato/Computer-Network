#include<iostream>
using namespace std;
void take_input(int arr[][3],int limit){
for(int i=0;i<limit;i++){
	cin>>arr[i][0];
	cin>>arr[i][1];
	cin>>arr[i][2];
}
}

void printVertices(int arr[][3],int dist[],int no_vertex){

for (int i = 1; i <= no_vertex; i++)
{
	if(dist[i]==100000){
	cout<<"x"<<" ";
	}
	else{
	cout<<dist[i]<<" ";

	}
}

}
void printTitle(int no_vertex){
	for(int i=1;i<=no_vertex;i++){ 
	cout<< i<<" ";
        // cout<<i<< " " <<dist[i]<<endl; 
}
}


int getMax(int dis[],int limit){
	int temp=dis[0];
	for (int i = 1; i <= limit; i++)
	{
		temp=max(temp,dis[i]);
	}
	return temp;
}

int bellman(int arr[][3],int start,int limit,int no_vertex){
int dist[no_vertex+1];
for(int i=1;i<=limit+1;i++){
dist[i]=100000;

}
dist[start]=0;
for(int i=1;i<=no_vertex-1;i++){
	cout<<" "<<endl;
	cout<<endl;
			cout<<i<<" iteration"<<endl;
			cout<<endl;
	printTitle(no_vertex);
	cout<<endl;
	for(int j=0;j<limit;j++){
		int u=arr[j][0];
		int v=arr[j][1];
		int w=arr[j][2];
			cout<<endl;
			printVertices(arr,dist,no_vertex);
		if(dist[u]!=100000 && dist[u]+w<dist[v] ){
			dist[v]=dist[u]+w;
		}
		

	}


}
return getMax(dist,limit+1);
}


int main(){
int nodes,arr[100][3],start,x;
cin>>nodes;
take_input(arr,nodes-1);
cin>>start;
x=bellman(arr,start,nodes-1,nodes);
cout<<endl;
cout<<x<<endl;
return 0;
}
