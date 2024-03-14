using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace 
{
    public class Solution_ZigzagConvert
    {
        public string Convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        
        StringBuilder sb = new StringBuilder();
        int cycleLen = 2 * numRows - 2;
        
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < s.Length; j += cycleLen) {
                sb.Append(s[j + i]);
                if (i > 0 && i < numRows - 1 && j + cycleLen - i < s.Length) {
                    sb.Append(s[j + cycleLen - i]);
                }
            }
        }
        
        return sb.ToString();
    }
        
    }
}