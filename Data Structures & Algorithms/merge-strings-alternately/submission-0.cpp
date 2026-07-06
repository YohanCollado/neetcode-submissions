class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        string answer;

        int i = 0;
        int j = 0;

        while (i < word1.length() && j < word2.length()){
            answer += word1[i++];
            answer += word2[j++];
        }

        answer += word1.substr(i);
        answer += word2.substr(j);
        return answer;
        
    }
};