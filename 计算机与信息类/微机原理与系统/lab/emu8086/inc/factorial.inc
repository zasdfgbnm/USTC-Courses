mulBig macro buffer  size  num
    ; num: db 
    ; buffer: db arr
    ; size : dw   length of buffer   
    local   zero,multiply,adjust, off,tmp ,skip_dcl 
    ;push di
    ;push si
    ;push ax
    ;push bx
    push cx 
    ;push dx   
    jmp skip_dcl       ; skip declaration                      
    tmp dw 10 dup(0)
    off dw 0
skip_dcl:  
    xor bh,bh
    mov bl,num 
    mov cx,size
    lea si,buffer 
    lea di,tmp
    add si,cx     
    
zero:
    dec si        
    cmp [si],0
    loope zero
                 
    mov cx,si                 
    lea si,buffer
    sub cx,si        
    inc cx
    mov off,cx  
    mov dx,0   
    
multiply:  
    xor ah,ah
    mov al,[si]
    mul bl 
    add dl,al
    mov [di],dx
    xor dh,dh
    mov dl,ah
    inc si
    add di,2
    loop multiply 
    
    mov [di],dx
    mov [di+2],00h 
    
    mov cx,off 
    lea si,tmp     
    lea di,buffer  
    mov bx,100h
adjust:  
    mov dx,0
    mov ax,[si]
    div bx
    add ax,[si+2]
    mov [si+2],ax
    mov [di],dx  
    inc di
    add si,2
    loop adjust
    
    mov [di],al     
    
    ;pop dx
    pop cx
    ;pop bx
    ;pop ax
    ;pop si
    ;pop di
mulBig endm

factorial macro n buffer size
    ; n:db
    ; buffer db arr
    local  fac
    push cx                     
    push si
    mov ch,0
    mov cl,n 
    lea si,buffer
    mov [si],1
fac:
   mulBig buffer size cl
   loop fac
   
   pop si
   pop cx
factorial endm