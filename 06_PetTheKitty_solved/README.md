use the deltapatch script with the png as input file, and the 2nd binary file as the patch. Trim the start of the patch file until PA30. 
The DLL shows tht the malware communicates via binary deltas. Extract all binary data sent to server in TCP stream 1 and run the script to get a transcript of all communications. 
The data is trivially encrypted using simple xor with `meoow` as the key array, encrypting each byte with the algorithm: index%length

`1m_H3rE_Liv3_1m_n0t_a_C4t@flare-on.com`
