Remove all inner functions using vim, using the following macro:

1. type `qqq` to clear all registers
2. type `/function<cr>f{da{dd@q` as seen

That should leave the relevant JS

Huge thanks to Yong Rong for creating the macro and making my life easier


We are then present with minimal JS that is the challenge.
All text after decryption routine should be ascii. hence, can write script to brute force each byte, to find out the possible candidates for each byte.
The script lowers the keyspace significantly, but some manual intervention is needed to get the full key.


key1: `ChVCVYzI1dU9cVg1ukBqO2u4UGr9aVCNWHpMUuYDLmDO22cdhXq3oqp8jmKBHUWI`

key2: `UQ8yjqwAkoVGm7VDdhLoDk0Q75eKKhTfXXke36UFdtKAi0etRZ3DoHPz7NxJPgHl`


`I_h4d_v1rtU411y_n0_r3h34rs4l_f0r_th4t@flare-on.com`
