#include <iostream>
#include <stdlib.h>
#include <limits>

using namespace std;

int main()
{
    string id;
    cout<<"Enter the variable name : "<<endl;
    cin>>id;
    int flag =0;
    

    for(int i =0;i<id.length();i++)
    {
        if(i==0)
        {
            if(id[i]=='_' || isalpha(id[i]))
            continue;
            else{
            flag=1;
            break;
            }
        }
        else if(i>0)
        {
            if(!isalnum(id[i]))
            {
                if(id[i]=='_')
                continue;
                else{
                 flag =1;
                 break;
                }
            }
        }
    

    }
      if(flag==1)
        cout<<"Not a valid variable name"<<endl;
        else
        cout<<"Valid variable name"<<endl;
        return 0;
}