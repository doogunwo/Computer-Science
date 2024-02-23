#include <iostream>
#include <string>
#include <stack>


bool isBalanced(const std::string& str){
    std::stack<char> s;

    for(char ch : str){
        if(ch == '(' || ch == '['){
            s.push(ch);
        }
        else if( ch== ')' || ch==']'){
            if(s.empty()) return false;
            char top = s.top();
            if((ch==')' && top=='(') || (ch==']') && ch=='[') {
                s.pop();
            }
            else{
                return false;
            }
        }
    }
    return s.empty();
}

int main(){

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    while(true){
        std::string str;
        std::getline(std::cin,str);

        if(str==".") break;
        if(isBalanced(str)){
            std::cout << "yes\n";
        }
        else{
            std::cout << "no\n";
        }
    }

    return 0;
}