#include <iostream>
#include <string>
#include <cmath>

class BinString
{
private:
  std::string binaryString;

public:
  BinString(std::string str) : binaryString(str) {}

  void showBinary()
  {
    std::cout << "Binary: ";
    for (char &ch : binaryString){
      if (ch == '1') {
        std::cout << "1";
      }
      else if (ch == '0') {
        std::cout << "0";
      }
    }
    std::cout << std::endl;
  }

  void showOctal()
  {
    long binaryLong = std::stol(binaryString);
    int octalNumber = 0, decimalNumber = 0, i = 0; 
    
    while(binaryLong != 0) { 
      decimalNumber += (binaryLong%10) * pow(2,i); ++i; 
      binaryLong/=10; 
    } 
    
    i = 1; 
    
    while (decimalNumber != 0) { 
      octalNumber += (decimalNumber % 8) * i; decimalNumber /= 8; i *= 10; 
    }

    std::cout << "Octal: " << octalNumber << std::endl;
  }

  int showDecimal(std::string source) {
    int decimal = 0;
    for (char& ch : source) {
      decimal = (decimal << 1) | (ch == '1' ? 1 : 0);
    }
    std::cout << "Decimal: " << decimal << std::endl;
    return decimal;
  }
  
  void showHex() {
    int decimal = showDecimal(binaryString);
    std::cout << "Hex: ";
    std::cout << std::hex << decimal << '\n';
  }
};

int main() {
  BinString bs("101010");

  bs.showBinary();
  bs.showOctal();
  bs.showDecimal("101010");
  bs.showHex();

  system("pause");

  return 0;
}