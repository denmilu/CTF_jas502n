n=2344088051
p=46099
q=50849 
e=65537
 
import primefac
d=primefac.modinv(e,(p-1)*(q-1))%((p-1)*(q-1))
 
v=[1]*100
v[15] = 622838535
v[16] = 0x1E53E463
v[17] = 0x217153B7
v[18] = 0xED044EB
v[19] = 0x26EC91AF
v[20] = 0x4F8C7090
v[21] = 0x45E4F9BB
v[22] = 0x26EC91AF
v[23] = 0x6D04B642
v[24] = 0x26EC91AF
v[25] = 0xFF559EE
v[26] = 0x1E53E463
v[27] = 0x55C81190
v[28] = 0x55C81190
v[29] = 0x58006440
v[30] = 0x217153B7
v[31] = 0x26EC91AF
v[32] = 0x35F1D9B2
v[33] = 0x4D3D8957
v[34] = 0x35F1D9B2
v[35] = 0x26EC91AF
v[36] = 0x7172720E
v[37] = 0x1E53E463
v[38] = 0x6AC5D9F7
v[39] = 0x58006440
v[40] = 0x4710F19D
v[41] = 653037999
v[42] = 1476420672
v[43] = 561075127
v[44] = 2095854527
v[45] = -2030465449
v[46] = 1439175056
v[47] = 1476420672
v[48] = 1439175056
v[49] = 653037999
v[50] = 508814435
v[51] = 561075127
v[52] = 653037999
v[53] = 839707766
v[54] = 1829025346
v[55] = 1751579215
v[56] = 1476420672
v[57] = 695921644
v[58] = 872207435
for i in range(15,59):
  print chr(pow(v[i],d,n)% 256) ,