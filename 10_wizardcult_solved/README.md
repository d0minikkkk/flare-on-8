The binary is the client application, which connects to the server via IRC. 

There are two handlers for the IRC. `main_main_func1` is triggered when the client connects, and `main_main_func2` is triggered when the PRIVMSG command is sent. A check is done in func2 to check if the targeted user is `dung3onm4st3r13`.

`wizardcult_comms_ProcessDMMessage` is then called to parse the message sent to the user.

The `wizardcult_tables_GetBytesFromTable` function is responsible for translating the words into opcodes which is then copied into a buffer, which is then passed into `wizardcult_vm_LoadProgram` to be run in the VM.

`wizardcult_tables_GetBytesFromTable` retrieves the index of the target word from the specified table and adds it to a new slice (index of a word maps to a single byte).

After `wizardcult_tables_GetBytesFromTable` is called to retrieve the indexes from the ingredients table, the buffer is passed into `wizardcult_vm_LoadProgram`, which create a byte buffer, create multiple channels, and sets up the VM components.
The ingredients make up a potion.

At the start of `wizardcult_vm_LoadProgram`, `encoding_gob___ptr_Decoder__Decode` is called with the address of vm_program, which transform a binary blob into a set of well-defined nested structures. `degob` can be used to reverse the process, and obtain the opcodes for each potion, revealing that each potion is actually a VM program.

when the `Potion of Water Breathing` is used, `wizardcult_potion_ReadFilePotion` function is called, and when the `Potion of Acid Resistence` is used, `wizardcult_potion_CommandPotion` function is called, while the dungeon descriptions appears to be commands. 

This suggests that the c2 server is instructing commands by giving descriptions of a dungeon, which performs a lookup of the respective potion to use, based on the dungeon to execute the commands. The VM is used to obfuscate/encrypt the data before it is sent back to the server as spell casting lines.

The c2 server can be mimicked by creating an IRC bot, to find out the mapping of each of plaintext to its ciphertext, generating a reverse lookup table.

The flag(png) encrypting cipher is a polyalphabetic cipher, with the key size of 24 bytes. Since each byte of input only affects a byte of output, a lookup table can generated by slowly building each byte in clocks of 24 bytes.

`wh0_n33ds_sw0rds_wh3n_you_h4ve_m4ge_h4nd@flare-on.com`