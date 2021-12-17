If you happen to have the recent yemeksepeti user information leaks, which is highly illegal so you shouldn't have it, follow these two steps to check if any of your contacts is in it.

1. Name the leak file as `list.txt`
2. `python3 numbers_from_attack.py` to extract numbers from the leak. (Uses Reg-Ex if you wonder)
3. Export your contact as .vcf file and put it in the same directory as the scripts.
4. Name the .vcf file `numbers.vcf`. (At the time I was building this project I was too lazy to implement arguements.
5. `python3 extract_vcf_and_check.py` to check if any of your contacts in the leak. This should print the numbers both in your contacts and in the leak

Just so you know, there are many different telephone number formats in use, I tried to parse the ones in my vcf file but don't be surprised if I missed some. 
