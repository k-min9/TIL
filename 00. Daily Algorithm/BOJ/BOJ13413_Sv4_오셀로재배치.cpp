#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    // 작업 횟수, 스트링 길이
    int tc, n;
    string before;
    string after;
    int Wcount = 0;
    int Bcount = 0;

    cin >> tc;
    while(tc--)
    {
        cin >> n >> before >> after;
        
        Wcount = 0;
        Bcount = 0;
        for(int i=0; i<n; i++)
        {
            // 비교하여 다를 경우 카운트 체크
            if(after.at(i) != before.at(i))
            {
                if(before.at(i) == 'W')
                    Wcount++;
                else
                    Bcount++;
            }
        }
        // 큰 쪽 을 출력하면 끝
        if(Wcount > Bcount)
            cout<<Wcount<<"\n";
        else
            cout<<Bcount<<"\n";

    }
    return 0;
}