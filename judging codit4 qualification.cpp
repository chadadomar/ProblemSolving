#include <iostream>
#include <regex>

using namespace std;
int main()
{
  int tt, iii;
  string a;
  regex e("A(KA)+");
  cin >> tt;
  while (tt--)
  {
    cin >> iii >> a;
    a = regex_replace(a, e, "");
    if (a.length() == 0)
      a = "EMPTY";
    cout << a << "\n";
  }
}
