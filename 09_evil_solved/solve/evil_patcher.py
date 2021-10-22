from binaryninja import *

target_opcodes = ['33c08b00', '33c0f7f0', '33fff7f7','33f6f7f6']

# change the address as needed
exception_handler_addr = 0x004054b0

call_eax = bv.arch.assemble('call eax')

bv.begin_undo_actions()

for opcode in target_opcodes:
    start_addr = bv.start
    while start_addr:
        start_addr = bv.find_next_data(start_addr+7, bytes.fromhex(opcode))
        if start_addr:
            print(f'[+] Found @ {hex(start_addr)}')

            # calculate call offset
            target_addr = (exception_handler_addr - start_addr) & 0xFFFFFFFF
            call_api_resolve = bv.arch.assemble(f'call {hex(target_addr)}')

            bv.write(start_addr, call_api_resolve)
            bv.write(start_addr+len(call_api_resolve),call_eax)

bv.commit_undo_actions()