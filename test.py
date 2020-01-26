# 64-bit	
# MOVBE	                            https://www.felixcloutier.com/x86/movbe
# MMX	
# SSE	
# SSE2	
# SSE3	
# SSSE3	
# SSE4.1	
# SSE4.2
# SSE4a (AMD)	
# POPCNT (AMD's ABM)	
# LZCNT (AMD's ABM)
# PKU	
# AVX	
# AVX2	
# AES	
# PCLMUL	
# FSGSBASE
# RDRND
# FMA3
# FMA4
# "ABM (AMD)"	
# BMI	
# BMI2	
# "TBM (AMD)"	
# F16C
# RDSEED
# ADCX
# PREFETCHW
# CLFLUSHOPT
# XSAVE?
# XSAVEOPT?
# XSAVEC
# XSAVES

# AVX512F
# AVX512PF?
# AVX512ER?
# AVX512VL
# AVX512BW
# AVX512DQ
# AVX512CD
# AVX5124VNNIW?
# AVX5124FMAPS?
# AVX512VBMI
# AVX512IFMA
# AVX512VBMI2
# AVX512VPOPCNTDQ
# AVX512BITALG
# AVX512VNNI
# AVX512BF16
# AVX512VP2INTERSECT

# SHA
# CLWB
# ENCLV?
# UMIP
# PTWRITE?
# RDPID
# SGX?
# GFNI
# GFNI-SSE?
# VPCLMULQDQ
# VAES
# PCONFIG
# WBNOINVD
# MOVDIRI
# MOVDIR64B
# BFLOAT16
# 3DNow!
# enhanced 3DNow!
# "SSE prefetch??? Parece que es una versón previa, no Full de SSE"	
# "XOP (AMD) ???"	
# "LWP (AMD) ???"	
# "CX16 (AMD) ???"	
# "MWAITX (AMD) ???"	
# "CLZERO (AMD) ???"
# "Extended MMX (AMD) https://en.wikipedia.org/wiki/Extended_MMX"
# PREFETCHWT1               #TODO(fernando): ver en qué marchs se usa...


#TODO(fernando) ---------------------------
# VMX               https://github.com/klauspost/cpuid/blob/master/cpuid.go#L866
# AESNI             https://github.com/klauspost/cpuid/blob/master/cpuid.go#L878
# PREFETCHWT1       ver en qué marchs se usa...



# http://instlatx64.atw.hu/
# https://github.com/klauspost/cpuid/blob/master/cpuid.go
# https://www.agner.org/optimize/#vectorclass
# https://github.com/vectorclass/version2/blob/master/instrset_detect.cpp

import cpuid
import base64
import string
import base58


# # x = base58.encode(37778931862960419483135)

# o = 37778931862960419483135
# print(o)
# x = base58.flex_encode(o)
# print(x)
# x_dec = base58.flex_decode(x)
# print(x_dec)


# # digs = string.digits + string.ascii_letters
# # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# digs = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
# print(digs)

# def int2base(x, base):
#     if x < 0:
#         sign = -1
#     elif x == 0:
#         return digs[0]
#     else:
#         sign = 1

#     x *= sign
#     digits = []

#     while x:
#         digits.append(digs[int(x % base)])
#         x = int(x / base)

#     if sign < 0:
#         digits.append('-')

#     digits.reverse()

#     return ''.join(digits)

# # import numpy
# print(37778931862960419483135)
# print(int2base(37778931862960419483135, 58))
# # numpy.base_repr(10, base=3)
# base94 = ''.join(map(chr, range(33,127)))
# print(base94)






# print(cpuid._is_long_mode_cpuid())
# ----------------------------------------------------------------------
#TODO(fernando): ponemos el Vendor o no en el entero?
# a, b, c, d = cpuid.cpuid(0)
# print(a)
# print(b)
# print(c)
# print(d)# 
# ----------------------------------------------------------------------


    # int info[4];
    # cpuid(info, 0);
    # int nIds = info[0];

    # cpuid(info, 0x80000000);
    # uint32_t nExIds = info[0];

    # //  Detect Features
    # if (nIds >= 0x00000001){
    #     cpuid(info, 0x00000001);
    #     HW_MMX    = (info[3] & ((int)1 << 23)) != 0;
    #     HW_SSE    = (info[3] & ((int)1 << 25)) != 0;
    #     HW_SSE2   = (info[3] & ((int)1 << 26)) != 0;
    #     HW_SSE3   = (info[2] & ((int)1 <<  0)) != 0;

    #     HW_SSSE3  = (info[2] & ((int)1 <<  9)) != 0;
    #     HW_SSE41  = (info[2] & ((int)1 << 19)) != 0;
    #     HW_SSE42  = (info[2] & ((int)1 << 20)) != 0;
    #     HW_AES    = (info[2] & ((int)1 << 25)) != 0;

    #     HW_AVX    = (info[2] & ((int)1 << 28)) != 0;
    #     HW_FMA3   = (info[2] & ((int)1 << 12)) != 0;

    #     HW_RDRAND = (info[2] & ((int)1 << 30)) != 0;
    # }

def reserved():
    return False

def max_function_id():
	a, _, _, _ = cpuid.cpuid(0)
	return a

def max_extended_function():
	a, _, _, _ = cpuid.cpuid(0x80000000)
	return a

def max_function_id():
	a, _, _, _ = cpuid.cpuid(0)
	return a

def support_movbe():
    # CPUID.01H:ECX.MOVBE[bit 22]
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & (1 << 22) != 0

def support_mmx():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L851
    if max_function_id() < 0x00000001: return False
    _, _, _, d = cpuid.cpuid(0x00000001)
    return d & (1 << 23) != 0

#TODO(fernando): la implementación de la librería de Golang creo que tiene un error, revisar y PR.
# def support_mmxext():
#     # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L854
#     if max_function_id() < 0x00000001: return False
#     _, _, _, d = cpuid.cpuid(0x00000001)
#     return d & (1 << 25) != 0

def support_sse():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L857
    if max_function_id() < 0x00000001: return False
    _, _, _, d = cpuid.cpuid(0x00000001)
    return d & (1 << 25) != 0

def support_sse2():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L860
    if max_function_id() < 0x00000001: return False
    _, _, _, d = cpuid.cpuid(0x00000001)
    return d & (1 << 26) != 0

def support_sse3():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L863
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & (1 << 0) != 0

def support_ssse3():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L869
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & 0x00000200 != 0

def support_sse41():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L872
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & 0x00080000 != 0

def support_sse42():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L875
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & 0x00100000 != 0

def support_sse4a():
    # CPUID.80000001H:ECX.SSE4A[Bit 6]
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L1022
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return c & (1 << 6) != 0

def support_popcnt():
    # https://github.com/klauspost/cpuid/blob/master/cpuid.go#L884
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & (1 << 23) != 0 or support_abm()

def support_abm():                  #lzcnt and popcnt
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return (c & (1 << 5)) != 0

def support_pku():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    # return (c & 0x00000008) != 0
    return (c & (1 << 3)) != 0

def support_avx_cpu():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 28)) != 0

def support_avx2_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 5)) != 0

def support_aes():                          # AES Native instructions
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 25)) != 0

def support_pclmul():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 1)) != 0

def support_fsgsbase():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 0)) != 0

def support_rdrnd():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 30)) != 0

def support_fma3_cpu():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 12)) != 0

def support_fma4_cpu():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return (c & (1 << 16)) != 0

def support_bmi():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 3)) != 0

def support_bmi2():
    if not support_bmi(): return False
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 3)) != 0

#TODO(fernando): check if CPU is AMD
# static bool TBM(void) { return CPU_Rep.isAMD_ && CPU_Rep.f_81_ECX_[21]; }
def support_tbm():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return (c & (1 << 21)) != 0

def support_f16c():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 29)) != 0

def support_rdseed():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 18)) != 0

# https://en.wikipedia.org/wiki/Intel_ADX
def support_adx():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 19)) != 0

# https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf
# pag. 202
# https://superuser.com/questions/931742/windows-10-64-bit-requirements-does-my-cpu-support-cmpxchg16b-prefetchw-and-la
def support_prefetchw():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return (c & (1 << 8)) != 0

def support_prefetchwt1():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 0)) != 0

def support_clflushopt():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 23)) != 0

def support_xsave_cpu():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 26)) != 0

def support_osxsave():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return (c & (1 << 27)) != 0

def support_xsaveopt_cpu():
    if max_function_id() < 0x0000000D: return False
    a, _, _, _ = cpuid.cpuid_count(0x0000000D, 1)
    return (a & (1 << 0)) != 0

def support_xsavec_cpu():
    if max_function_id() < 0x0000000D: return False
    a, _, _, _ = cpuid.cpuid_count(0x0000000D, 1)
    return (a & (1 << 1)) != 0

def support_xsaves_cpu():
    if max_function_id() < 0x0000000D: return False
    a, _, _, _ = cpuid.cpuid_count(0x0000000D, 1)
    return (a & (1 << 3)) != 0

def support_avx512f_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 16)) != 0

def support_avx512pf_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 26)) != 0

def support_avx512er_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 27)) != 0

def support_avx512vl_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 31)) != 0

def support_avx512bw_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 30)) != 0

def support_avx512dq_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 17)) != 0

def support_avx512cd_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 28)) != 0

def support_avx5124vnniw_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, _, d = cpuid.cpuid(0x00000007)
    _, _, _, d = cpuid.cpuid_count(7, 0)
    return (d & (1 << 2)) != 0

def support_avx5124fmaps_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, _, d = cpuid.cpuid(0x00000007)
    _, _, _, d = cpuid.cpuid_count(7, 0)
    return (d & (1 << 3)) != 0

def support_avx512vbmi_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 1)) != 0

def support_avx512ifma_cpu():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 21)) != 0

def support_avx512vbmi2_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 6)) != 0

def support_avx512vpopcntdq_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 14)) != 0

def support_avx512bitalg_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 12)) != 0

def support_avx512vnni_cpu():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 11)) != 0

def support_avx512bf16_cpu():
    #TODO(fernando): is it ok to check the max_function_id() < 0x00000007 for calling cpuid_count(7, 1) ?
    if max_function_id() < 0x00000007: return False
    a, _, _, _ = cpuid.cpuid_count(7, 1)
    return (a & (1 << 5)) != 0

def support_avx512vp2intersect_cpu():
    return False #TODO(fernando) ... bit_AVX512VP2INTERSECT
    # if max_function_id() < 0x00000007: return False
    ## _, _, _, d = cpuid.cpuid(0x00000007)
    # _, _, _, d = cpuid.cpuid_count(7, 0)
    # return (d & (1 << 3)) != 0

def support_sha():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 29)) != 0

def support_clwb():
    if max_function_id() < 0x00000007: return False
    # _, b, _, _ = cpuid.cpuid(0x00000007)
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 24)) != 0

# TODO(fernando): ver Enclave en Golang
def support_enclv():
    return False

def support_umip():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 2)) != 0

# TODO(fernando): PTWRITE?
def support_ptwrite():
    return False

def support_rdpid():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 22)) != 0

# TODO(fernando): SGX?           
# Ver SGX en Golang
def support_sgx():
    return False

def support_gfni():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 8)) != 0

# TODO(fernando): GFNI-SSE?          
def support_gfni_sse():
    return False

def support_vpclmulqdq():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 10)) != 0

def support_vaes():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 9)) != 0

def support_pconfig():
    if max_function_id() < 0x00000007: return False
    # _, _, _, d = cpuid.cpuid(0x00000007)
    _, _, _, d = cpuid.cpuid_count(7, 0)
    return (d & (1 << 18)) != 0

# TODO(fernando): WBNOINVD       
def support_wbnoinvd():
    return False

#TODO(fernando): GCC hace referencia a MOVDIRI, está relacionado a MOVDIR?
def support_movdir():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 27)) != 0

def support_movdir64b():
    if max_function_id() < 0x00000007: return False
    # _, _, c, _ = cpuid.cpuid(0x00000007)
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 28)) != 0

# TODO(fernando): BFLOAT16       
def support_bfloat16():
    return False

def support_3dnow():
    if max_extended_function() < 0x80000001: return False
    _, _, _, d = cpuid.cpuid(0x80000001)
    return d & (1 << 31) != 0

# enhanced 3DNow!
def support_3dnowext():
    if max_extended_function() < 0x80000001: return False
    _, _, _, d = cpuid.cpuid(0x80000001)
    return d & (1 << 30) != 0

#TODO(fernando): GCC muestra como "SSE prefetch"
    # ‘athlon-tbird’
    # AMD Athlon CPU with MMX, 3dNOW!, enhanced 3DNow! and SSE prefetch instructions support.
# creo que se refiere a lo mismo
def support_3dnowprefetch():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return c & (1 << 8) != 0

def support_xop():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return c & (1 << 11) != 0

def support_lwp():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return c & (1 << 15) != 0

# CMPXCHG16B
def support_cx16():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & (1 << 13) != 0

#TODO(fernando): GCC hace referencia a MWAITX, creemos que es lo mismo
def support_mwait():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)
    return c & (1 << 3) != 0

# TODO(fernando): CLZERO       (AMD) 
def support_clzero():
    return False

# "Extended MMX (AMD) https://en.wikipedia.org/wiki/Extended_MMX"
def support_mmxext():
    if max_extended_function() < 0x80000001: return False
    _, _, _, d = cpuid.cpuid(0x80000001)
    return d & (1 << 22) != 0





# -----------------------------------------------------------------
# OS support
# -----------------------------------------------------------------

# https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Operating_system_support
def support_avx_os():
    # Copied from: http://stackoverflow.com/a/22521619/922184

    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)

    XGETBV = (c & (1 << 26)) != 0
    osUsesXSAVE_XRSTORE = (c & (1 << 27)) != 0
    cpuAVXSuport = (c & (1 << 28)) != 0

    if not (XGETBV and osUsesXSAVE_XRSTORE and cpuAVXSuport):
        return False

    xcrFeatureMask = cpuid.xgetbv(0)
    return (xcrFeatureMask & 0x6) == 0x6

def support_avx2_os():
    return support_avx_os() and support_avx2_cpu()

def support_fma3_os():
    return support_avx_os() and support_fma3_cpu()

def support_fma4_os():
    return support_avx_os() and support_fma4_cpu()

def support_xsave_os():
    return support_xsave_cpu() and support_osxsave()

def support_xsaveopt_os():
    return support_xsaveopt_cpu() and support_xsave_os()

def support_xsavec_os():
    return support_xsavec_cpu() and support_xsave_os()

def support_xsaves_os():
    return support_xsaves_cpu() and support_xsave_os()

def support_avx512_os():
    if max_function_id() < 0x00000001: return False
    _, _, c, _ = cpuid.cpuid(0x00000001)

    # Only detect AVX-512 features if XGETBV is supported
    if c & ((1<<26)|(1<<27)) != (1<<26)|(1<<27): return False

    # Check for OS support
    eax = cpuid.xgetbv(0)

    # Verify that XCR0[7:5] = ‘111b’ (OPMASK state, upper 256-bit of ZMM0-ZMM15 and
    # ZMM16-ZMM31 state are enabled by OS)
    #  and that XCR0[2:1] = ‘11b’ (XMM state and YMM state are enabled by OS).
    return (eax>>5)&7 == 7 and (eax>>1)&3 == 3

def support_avx512f_os():
    return support_avx512_os() and support_avx512f_cpu()

def support_avx512pf_os():
    return support_avx512_os() and support_avx512pf_cpu()

def support_avx512er_os():
    return support_avx512_os() and support_avx512er_cpu()

def support_avx512vl_os():
    return support_avx512_os() and support_avx512vl_cpu()

def support_avx512bw_os():
    return support_avx512_os() and support_avx512bw_cpu()

def support_avx512dq_os():
    return support_avx512_os() and support_avx512dq_cpu()

def support_avx512cd_os():
    return support_avx512_os() and support_avx512cd_cpu()

def support_avx5124vnniw_os():
    return support_avx512_os() and support_avx5124vnniw_cpu()

def support_avx5124fmaps_os():
    return support_avx512_os() and support_avx5124fmaps_cpu()

def support_avx512vbmi_os():
    return support_avx512_os() and support_avx512vbmi_cpu()

def support_avx512ifma_os():
    return support_avx512_os() and support_avx512ifma_cpu()

def support_avx512vbmi2_os():
    return support_avx512_os() and support_avx512vbmi2_cpu()

def support_avx512vpopcntdq_os():
    return support_avx512_os() and support_avx512vpopcntdq_cpu()

def support_avx512bitalg_os():
    return support_avx512_os() and support_avx512bitalg_cpu()

def support_avx512vnni_os():
    return support_avx512_os() and support_avx512vnni_cpu()

def support_avx512bf16_os():
    return support_avx512_os() and support_avx512bf16_cpu()

def support_avx512vp2intersect_os():
    return support_avx512_os() and support_avx512vp2intersect_cpu()



# -----------------------------------------------------------------


instructions_map = {
    0:   cpuid._is_long_mode_cpuid,
    1:   support_movbe,
    2:   support_mmx,
    3:   support_sse,
    4:   support_sse2,
    5:   support_sse3,
    6:   support_ssse3,
    7:   support_sse41,
    8:   support_sse42,
    9:   support_sse4a,
    10:  support_popcnt,
    11:  support_abm,
    12:  support_pku,
    13:  support_avx_os,
    14:  support_avx2_os,
    15:  support_aes,
    16:  support_pclmul,
    17:  support_fsgsbase,
    18:  support_rdrnd,
    19:  support_fma3_os,
    20:  support_fma4_os,
    21:  support_abm,
    22:  support_bmi,
    23:  support_bmi2,
    24:  support_tbm,
    25:  support_f16c,
    26:  support_rdseed,
    27:  support_adx,
    28:  support_prefetchw,
    29:  support_clflushopt,
    30:  support_xsave_os,
    31:  support_xsaveopt_os,
    32:  support_xsavec_os,
    33:  support_xsaves_os,

    34:  support_avx512f_os,
    35:  support_avx512pf_os,
    36:  support_avx512er_os,
    37:  support_avx512vl_os,
    38:  support_avx512bw_os,
    39:  support_avx512dq_os,
    40:  support_avx512cd_os,
    41:  support_avx5124vnniw_os,
    42:  support_avx5124fmaps_os,
    43:  support_avx512vbmi_os,
    44:  support_avx512ifma_os,
    45:  support_avx512vbmi2_os,
    46:  support_avx512vpopcntdq_os,
    47:  support_avx512bitalg_os,
    48:  support_avx512vnni_os,
    49:  support_avx512bf16_os,
    50:  support_avx512vp2intersect_os,

    51:  support_sha,
    52:  support_clwb,
    53:  support_enclv,
    54:  support_umip,
    55:  support_ptwrite,
    56:  support_rdpid,
    57:  support_sgx,
    58:  support_gfni,
    59:  support_gfni_sse,
    60:  support_vpclmulqdq,
    61:  support_vaes,
    62:  support_pconfig,
    63:  support_wbnoinvd,
    64:  support_movdir,
    65:  support_movdir64b,
    66:  support_bfloat16,
    67:  support_3dnow,
    68:  support_3dnowext,
    69:  support_3dnowprefetch,
    70:  support_xop,
    71:  support_lwp,
    72:  support_cx16,
    73:  support_mwait,
    74:  support_clzero,
    75:  support_mmxext,
    76:  support_prefetchwt1,

    77:  reserved,
    78:  reserved,
    79:  reserved,
    80:  reserved,
    81:  reserved,
    82:  reserved,
    83:  reserved,
    84:  reserved,
    85:  reserved,
    86:  reserved,
    87:  reserved,
    88:  reserved,
    89:  reserved,
    90:  reserved,
    91:  reserved,
    92:  reserved,
    93:  reserved,
    94:  reserved,
    95:  reserved,
    96:  reserved,
    97:  reserved,
    98:  reserved,
    99:  reserved,
    100: reserved,
    101: reserved,
    102: reserved,
    103: reserved,
    104: reserved,
    105: reserved,
    106: reserved,
    107: reserved,
    108: reserved,
    109: reserved,
    110: reserved,
    111: reserved,
    112: reserved,
    113: reserved,
    114: reserved,
    115: reserved,
    116: reserved,
    117: reserved,
    118: reserved,
    119: reserved,
    120: reserved,
    121: reserved,
    122: reserved,
    123: reserved,
    124: reserved,
    125: reserved,
    126: reserved,
    127: reserved,
    128: reserved,
    129: reserved,
    130: reserved,
    131: reserved,
    132: reserved,
    133: reserved,
    134: reserved,
    135: reserved,
    136: reserved,
    137: reserved,
    138: reserved,
    139: reserved,
    140: reserved,
    141: reserved,
    142: reserved,
    143: reserved,
    144: reserved,
    145: reserved,
    146: reserved,
    147: reserved,
    148: reserved,
    149: reserved,
    150: reserved,
    151: reserved,
    152: reserved,
    153: reserved,
    154: reserved,
    155: reserved,
    156: reserved,
    157: reserved,
    158: reserved,
    159: reserved,
    160: reserved,
    161: reserved,
    162: reserved,
    163: reserved,
    164: reserved,
    165: reserved,
    166: reserved,
    167: reserved,
    168: reserved,
    169: reserved,
    170: reserved,
    171: reserved,
    172: reserved,
    173: reserved,
    174: reserved,
    175: reserved,
    176: reserved,
    177: reserved,
    178: reserved,
    179: reserved,
    180: reserved,
    181: reserved,
    182: reserved,
    183: reserved,
    184: reserved,
    185: reserved,
    186: reserved,
    187: reserved,
    188: reserved,
    189: reserved,
    190: reserved,
    191: reserved,
    192: reserved,
    193: reserved,
    194: reserved,
    195: reserved,
    196: reserved,
    197: reserved,
    198: reserved,
    199: reserved,
    200: reserved,
    201: reserved,
    202: reserved,
    203: reserved,
    204: reserved,
    205: reserved,
    206: reserved,
    207: reserved,
    208: reserved,
    209: reserved,
    210: reserved,
    211: reserved,
    212: reserved,
    213: reserved,
    214: reserved,
    215: reserved,
    216: reserved,
    217: reserved,
    218: reserved,
    219: reserved,
    220: reserved,
    221: reserved,
    222: reserved,
    223: reserved,
    224: reserved,
    225: reserved,
    226: reserved,
    227: reserved,
    228: reserved,
    229: reserved,
    230: reserved,
    231: reserved,
    232: reserved,
    233: reserved,
    234: reserved,
    235: reserved,
    236: reserved,
    237: reserved,
    238: reserved,
    239: reserved,
    240: reserved,
    241: reserved,
    242: reserved,
    243: reserved,
    244: reserved,
    245: reserved,
    246: reserved,
    247: reserved,
    248: reserved,
    249: reserved,
    250: reserved,
    251: reserved,
    252: reserved,
    253: reserved,
    254: reserved,
    255: reserved,
}

instructions_names = {
    0:   "64 bits",
    1:   "movbe",
    2:   "mmx",
    3:   "sse",
    4:   "sse2",
    5:   "sse3",
    6:   "ssse3",
    7:   "sse41",
    8:   "sse42",
    9:   "sse4a",
    10:  "popcnt",
    11:  "abm",
    12:  "pku",
    13:  "avx",
    14:  "avx2",
    15:  "aes",
    16:  "pclmul",
    17:  "fsgsbase",
    18:  "rdrnd",
    19:  "fma3",
    20:  "fma4",
    21:  "abm",
    22:  "bmi",
    23:  "bmi2",
    24:  "tbm",
    25:  "f16c",
    26:  "rdseed",
    27:  "adx",
    28:  "prefetchw",
    29:  "clflushopt",
    30:  "xsave",
    31:  "xsaveopt",
    32:  "xsavec",
    33:  "xsaves",

    34:  "avx512f",
    35:  "avx512pf",
    36:  "avx512er",
    37:  "avx512vl",
    38:  "avx512bw",
    39:  "avx512dq",
    40:  "avx512cd",
    41:  "avx5124vnniw",
    42:  "avx5124fmaps",
    43:  "avx512vbmi",
    44:  "avx512ifma",
    45:  "avx512vbmi2",
    46:  "avx512vpopcntdq",
    47:  "avx512bitalg",
    48:  "avx512vnni",
    49:  "avx512bf16",
    50:  "avx512vp2intersect",

    51:  "sha",
    52:  "clwb",
    53:  "enclv",
    54:  "umip",
    55:  "ptwrite",
    56:  "rdpid",
    57:  "sgx",
    58:  "gfni",
    59:  "gfni_sse",
    60:  "vpclmulqdq",
    61:  "vaes",
    62:  "pconfig",
    63:  "wbnoinvd",
    64:  "movdir",
    65:  "movdir64b",
    66:  "bfloat16",
    67:  "3dnow",
    68:  "3dnowext",
    69:  "3dnowprefetch",
    70:  "xop",
    71:  "lwp",
    72:  "cx16",
    73:  "mwait",
    74:  "clzero",
    75:  "mmxext",
    76:  "prefetchwt1",

    77:  "__reserved__",
    78:  "__reserved__",
    79:  "__reserved__",
    80:  "__reserved__",
    81:  "__reserved__",
    82:  "__reserved__",
    83:  "__reserved__",
    84:  "__reserved__",
    85:  "__reserved__",
    86:  "__reserved__",
    87:  "__reserved__",
    88:  "__reserved__",
    89:  "__reserved__",
    90:  "__reserved__",
    91:  "__reserved__",
    92:  "__reserved__",
    93:  "__reserved__",
    94:  "__reserved__",
    95:  "__reserved__",
    96:  "__reserved__",
    97:  "__reserved__",
    98:  "__reserved__",
    99:  "__reserved__",
    100: "__reserved__",
    101: "__reserved__",
    102: "__reserved__",
    103: "__reserved__",
    104: "__reserved__",
    105: "__reserved__",
    106: "__reserved__",
    107: "__reserved__",
    108: "__reserved__",
    109: "__reserved__",
    110: "__reserved__",
    111: "__reserved__",
    112: "__reserved__",
    113: "__reserved__",
    114: "__reserved__",
    115: "__reserved__",
    116: "__reserved__",
    117: "__reserved__",
    118: "__reserved__",
    119: "__reserved__",
    120: "__reserved__",
    121: "__reserved__",
    122: "__reserved__",
    123: "__reserved__",
    124: "__reserved__",
    125: "__reserved__",
    126: "__reserved__",
    127: "__reserved__",
    128: "__reserved__",
    129: "__reserved__",
    130: "__reserved__",
    131: "__reserved__",
    132: "__reserved__",
    133: "__reserved__",
    134: "__reserved__",
    135: "__reserved__",
    136: "__reserved__",
    137: "__reserved__",
    138: "__reserved__",
    139: "__reserved__",
    140: "__reserved__",
    141: "__reserved__",
    142: "__reserved__",
    143: "__reserved__",
    144: "__reserved__",
    145: "__reserved__",
    146: "__reserved__",
    147: "__reserved__",
    148: "__reserved__",
    149: "__reserved__",
    150: "__reserved__",
    151: "__reserved__",
    152: "__reserved__",
    153: "__reserved__",
    154: "__reserved__",
    155: "__reserved__",
    156: "__reserved__",
    157: "__reserved__",
    158: "__reserved__",
    159: "__reserved__",
    160: "__reserved__",
    161: "__reserved__",
    162: "__reserved__",
    163: "__reserved__",
    164: "__reserved__",
    165: "__reserved__",
    166: "__reserved__",
    167: "__reserved__",
    168: "__reserved__",
    169: "__reserved__",
    170: "__reserved__",
    171: "__reserved__",
    172: "__reserved__",
    173: "__reserved__",
    174: "__reserved__",
    175: "__reserved__",
    176: "__reserved__",
    177: "__reserved__",
    178: "__reserved__",
    179: "__reserved__",
    180: "__reserved__",
    181: "__reserved__",
    182: "__reserved__",
    183: "__reserved__",
    184: "__reserved__",
    185: "__reserved__",
    186: "__reserved__",
    187: "__reserved__",
    188: "__reserved__",
    189: "__reserved__",
    190: "__reserved__",
    191: "__reserved__",
    192: "__reserved__",
    193: "__reserved__",
    194: "__reserved__",
    195: "__reserved__",
    196: "__reserved__",
    197: "__reserved__",
    198: "__reserved__",
    199: "__reserved__",
    200: "__reserved__",
    201: "__reserved__",
    202: "__reserved__",
    203: "__reserved__",
    204: "__reserved__",
    205: "__reserved__",
    206: "__reserved__",
    207: "__reserved__",
    208: "__reserved__",
    209: "__reserved__",
    210: "__reserved__",
    211: "__reserved__",
    212: "__reserved__",
    213: "__reserved__",
    214: "__reserved__",
    215: "__reserved__",
    216: "__reserved__",
    217: "__reserved__",
    218: "__reserved__",
    219: "__reserved__",
    220: "__reserved__",
    221: "__reserved__",
    222: "__reserved__",
    223: "__reserved__",
    224: "__reserved__",
    225: "__reserved__",
    226: "__reserved__",
    227: "__reserved__",
    228: "__reserved__",
    229: "__reserved__",
    230: "__reserved__",
    231: "__reserved__",
    232: "__reserved__",
    233: "__reserved__",
    234: "__reserved__",
    235: "__reserved__",
    236: "__reserved__",
    237: "__reserved__",
    238: "__reserved__",
    239: "__reserved__",
    240: "__reserved__",
    241: "__reserved__",
    242: "__reserved__",
    243: "__reserved__",
    244: "__reserved__",
    245: "__reserved__",
    246: "__reserved__",
    247: "__reserved__",
    248: "__reserved__",
    249: "__reserved__",
    250: "__reserved__",
    251: "__reserved__",
    252: "__reserved__",
    253: "__reserved__",
    254: "__reserved__",
    255: "__reserved__",
}

def get_available_instructions():
    data = []
    for _, f in instructions_map.items():
        # data.append(str(int(f())))
        data.append(int(f()))
    return data

def _to_chars_bin(data):
    res = []
    for x in data:
        res.append(str(x))
    return res

def _to_ints_bin(data):
    res = []
    for x in data:
        res.append(int(x))
    return res

def _pad_right_array(data):
    if len(data) >= len(instructions_map): return data
    n = len(instructions_map) - len(data)
    for i in range(n):
        data.append(int(0))
    return data

def encode_instructions(insts):
    insts = _to_chars_bin(insts)
    insts_str = ''.join(reversed(insts))
    insts_num = int(insts_str, 2)
    insts_num_b58 = base58.flex_encode(insts_num)
    return insts_num_b58

def decode_instructions(architecture_id):
    insts_num = base58.flex_decode(architecture_id)
    res = "{0:b}".format(insts_num)
    res = res.zfill(len(instructions_map))
    return _to_ints_bin([*reversed(res)])
    # return [*reversed(res)]

def get_architecture_id():
    insts = get_available_instructions()
    architecture_id = encode_instructions(insts)
    return architecture_id

def print_available_extensions(exts):
    for i in range(len(exts)):
        if (exts[i] == 1):
            print("your computer supports " + instructions_names[i])

print("CPUID Microarchitecture : %s%s" % cpuid.cpu_microarchitecture())
architecture_id = get_architecture_id()
print("architecture_id: %s" % architecture_id)

insts = get_available_instructions()
print(insts)

