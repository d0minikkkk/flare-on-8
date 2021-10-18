Viewing the cronjobs of the VM reveals a binary and the method used to encrypt files in the documents directory. Each char of each file is XORed using a lookup table modified at runtime. Good news is that the lookup table can be reimplemented using the same algorithm at each iteration. Given that the encryption is just XOR, the binary's encryption algorithm could pretty much be reused for decrypton. 
Upon decrypting the files, follow the hints in each file to get pieces of the password.

A bruteforce script was written as some bytes were unclear due to bad decryption(?) or unknown answers to questions in the hints. Since only 2 bytes were unknown, the bruteforce script runs relatively quickly

`H4Ck3r_e5c4P3D@flare-on.com`