#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    int a,b;
    a= b= 0;
    for(int i=0; i<num_list.size(); i++){
        if (num_list[i] %2 == 0){
            a += 1;
            
        }
        else{
            b += 1;
        }
        
    }

    answer.push_back(a);
    answer.push_back(b);
    return answer;
}