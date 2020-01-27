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


# ------------------------------------------------------------------------------------
#TODO(fernando): chequear las siguientes instrucciones a ver si las soportamos
	# CMOV:               "CMOV",               // i686 CMOV
	# NX:                 "NX",                 // NX (No-Execute) bit
	# AMD3DNOW:           "AMD3DNOW",           // AMD 3DNOW
	# AMD3DNOWEXT:        "AMD3DNOWEXT",        // AMD 3DNowExt
	# MMX:                "MMX",                // Standard MMX
	# MMXEXT:             "MMXEXT",             // SSE integer functions or AMD MMX ext
	# SSE:                "SSE",                // SSE functions
	# SSE2:               "SSE2",               // P4 SSE2 functions
	# SSE3:               "SSE3",               // Prescott SSE3 functions
	# SSSE3:              "SSSE3",              // Conroe SSSE3 functions
	# SSE4:               "SSE4.1",             // Penryn SSE4.1 functions
	# SSE4A:              "SSE4A",              // AMD Barcelona microarchitecture SSE4a instructions
	# SSE42:              "SSE4.2",             // Nehalem SSE4.2 functions
	# AVX:                "AVX",                // AVX functions
	# AVX2:               "AVX2",               // AVX functions
	# FMA3:               "FMA3",               // Intel FMA 3
	# FMA4:               "FMA4",               // Bulldozer FMA4 functions
	# XOP:                "XOP",                // Bulldozer XOP functions
	# F16C:               "F16C",               // Half-precision floating-point conversion
	# BMI1:               "BMI1",               // Bit Manipulation Instruction Set 1
	# BMI2:               "BMI2",               // Bit Manipulation Instruction Set 2
	# TBM:                "TBM",                // AMD Trailing Bit Manipulation
	# LZCNT:              "LZCNT",              // LZCNT instruction
	# POPCNT:             "POPCNT",             // POPCNT instruction
	# AESNI:              "AESNI",              // Advanced Encryption Standard New Instructions
	# CLMUL:              "CLMUL",              // Carry-less Multiplication
	# HTT:                "HTT",                // Hyperthreading (enabled)
	# HLE:                "HLE",                // Hardware Lock Elision
	# RTM:                "RTM",                // Restricted Transactional Memory
	# RDRAND:             "RDRAND",             // RDRAND instruction is available
	# RDSEED:             "RDSEED",             // RDSEED instruction is available
	# ADX:                "ADX",                // Intel ADX (Multi-Precision Add-Carry Instruction Extensions)
	# SHA:                "SHA",                // Intel SHA Extensions
	# AVX512F:            "AVX512F",            // AVX-512 Foundation
	# AVX512DQ:           "AVX512DQ",           // AVX-512 Doubleword and Quadword Instructions
	# AVX512IFMA:         "AVX512IFMA",         // AVX-512 Integer Fused Multiply-Add Instructions
	# AVX512PF:           "AVX512PF",           // AVX-512 Prefetch Instructions
	# AVX512ER:           "AVX512ER",           // AVX-512 Exponential and Reciprocal Instructions
	# AVX512CD:           "AVX512CD",           // AVX-512 Conflict Detection Instructions
	# AVX512BW:           "AVX512BW",           // AVX-512 Byte and Word Instructions
	# AVX512VL:           "AVX512VL",           // AVX-512 Vector Length Extensions
	# AVX512VBMI:         "AVX512VBMI",         // AVX-512 Vector Bit Manipulation Instructions
	# AVX512VBMI2:        "AVX512VBMI2",        // AVX-512 Vector Bit Manipulation Instructions, Version 2
	# AVX512VNNI:         "AVX512VNNI",         // AVX-512 Vector Neural Network Instructions
	# AVX512VPOPCNTDQ:    "AVX512VPOPCNTDQ",    // AVX-512 Vector Population Count Doubleword and Quadword
	# GFNI:               "GFNI",               // Galois Field New Instructions
	# VAES:               "VAES",               // Vector AES
	# AVX512BITALG:       "AVX512BITALG",       // AVX-512 Bit Algorithms
	# VPCLMULQDQ:         "VPCLMULQDQ",         // Carry-Less Multiplication Quadword
	# AVX512BF16:         "AVX512BF16",         // AVX-512 BFLOAT16 Instruction
	# AVX512VP2INTERSECT: "AVX512VP2INTERSECT", // AVX-512 Intersect for D/Q
	# MPX:                "MPX",                // Intel MPX (Memory Protection Extensions)
	# ERMS:               "ERMS",               // Enhanced REP MOVSB/STOSB
	# RDTSCP:             "RDTSCP",             // RDTSCP Instruction
	# CX16:               "CX16",               // CMPXCHG16B Instruction
	# SGX:                "SGX",                // Software Guard Extensions
	# SGXLC:              "SGXLC",              // Software Guard Extensions Launch Control
	# IBPB:               "IBPB",               // Indirect Branch Restricted Speculation and Indirect Branch Predictor Barrier
	# STIBP:              "STIBP",              // Single Thread Indirect Branch Predictors
	# VMX:                "VMX",                // Virtual Machine Extensions

	# // Performance indicators
	# SSE2SLOW: "SSE2SLOW", // SSE2 supported, but usually not faster
	# SSE3SLOW: "SSE3SLOW", // SSE3 supported, but usually not faster
	# ATOM:     "ATOM",     // Atom processor, some SSSE3 instructions are slower
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
#TODO(fernando): Faltan implementar
# Provienen de GCC: https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html

# -mprfchw
# -mfxsr
# -mrtm
# -mhle
# -mwaitpkg
# -menqcmd
# -mcldemote
# -mcld
# -mvzeroupper
# -msahf
# -mshstk
# -mcrc32
# -mrecip
 
# ------------------------------------------------------------------------------------
#TODO(fernando): ver todas las instrucciones que se usan en el proyecto QEMU

# ------------------------------------------------------------------------------------






#TODO(fernando) ---------------------------
# VMX               https://github.com/klauspost/cpuid/blob/master/cpuid.go#L866
# AESNI             https://github.com/klauspost/cpuid/blob/master/cpuid.go#L878
# PREFETCHWT1       ver en qué marchs se usa...



# http://instlatx64.atw.hu/
# https://github.com/klauspost/cpuid/blob/master/cpuid.go
# https://www.agner.org/optimize/#vectorclass
# https://github.com/vectorclass/version2/blob/master/instrset_detect.cpp
# https://hjlebbink.github.io/x86doc/
# https://software.intel.com/sites/default/files/managed/c5/15/architecture-instruction-set-extensions-programming-reference.pdf

import cpuid
import base64
import string
import base58
from enum import Enum


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

#Note(fernando): check if CPU is AMD, I think it is not necessary
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
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 1)) != 0

def support_avx512ifma_cpu():
    if max_function_id() < 0x00000007: return False
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 21)) != 0

def support_avx512vbmi2_cpu():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 6)) != 0

def support_avx512vpopcntdq_cpu():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 14)) != 0

def support_avx512bitalg_cpu():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 12)) != 0

def support_avx512vnni_cpu():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 11)) != 0

def support_avx512bf16_cpu():
    if max_function_id() < 0x00000007: return False
    a, _, _, _ = cpuid.cpuid_count(7, 1)
    return (a & (1 << 5)) != 0

def support_avx512vp2intersect_cpu():
    if max_function_id() < 0x00000007: return False
    _, _, _,d = cpuid.cpuid_count(7, 0)
    return (d & (1 << 8)) != 0

def support_sha():
    if max_function_id() < 0x00000007: return False
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 29)) != 0

def support_clwb():
    if max_function_id() < 0x00000007: return False
    _, b, _, _ = cpuid.cpuid_count(7, 0)
    return (b & (1 << 24)) != 0

# TODO(fernando): ver Enclave en Golang
def support_enclv():
    return False

def support_umip():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 2)) != 0

# https://hjlebbink.github.io/x86doc/html/PTWRITE.html
def support_ptwrite():
    # TODO(fernando): chequear que sea correcto
    # If CPUID.(EAX=14H, ECX=0):EBX.PTWRITE [Bit 4] = 0.
    # If LOCK prefix is used.
    # If 66H prefix is used.
    if max_function_id() < 0x00000014: return False
    _, b, _, _ = cpuid.cpuid_count(0x00000014, 0)
    return (b & (1 << 4)) != 0

def support_rdpid():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 22)) != 0

# TODO(fernando): SGX?           
# Ver SGX en Golang
def support_sgx():
    return False

def support_gfni():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 8)) != 0

# https://software.intel.com/en-us/forums/intel-isa-extensions/topic/810449
def support_gfni_sse():
    return support_gfni()

def support_vpclmulqdq():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 10)) != 0

def support_vaes():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 9)) != 0

def support_pconfig():
    if max_function_id() < 0x00000007: return False
    _, _, _, d = cpuid.cpuid_count(7, 0)
    return (d & (1 << 18)) != 0

def support_wbnoinvd():
    if max_extended_function() < 0x80000008: return False
    _, b, _, _ = cpuid.cpuid(0x80000008)
    return (b & (1 << 9)) != 0

#https://www.felixcloutier.com/x86/movdiri
def support_movdir():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 27)) != 0

def support_movdir64b():
    if max_function_id() < 0x00000007: return False
    _, _, c, _ = cpuid.cpuid_count(7, 0)
    return (c & (1 << 28)) != 0

# https://www.extremetech.com/computing/296246-intel-announces-cooper-lake-will-be-socketed-compatible-with-future-ice-lake-cpus
# TODO(fernando): ver si hay diferencia entre avx512bf16 y bfloat16  
# cooperlake y tigerlake       
def support_bfloat16():
    return support_avx512bf16_os()

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

# def support_mwait():
#     if max_function_id() < 0x00000001: return False
#     _, _, c, _ = cpuid.cpuid(0x00000001)
#     return c & (1 << 3) != 0

# https://reviews.llvm.org/rL269911
def support_mwaitx():
    if max_extended_function() < 0x80000001: return False
    _, _, c, _ = cpuid.cpuid(0x80000001)
    return c & (1 << 29) != 0

# https://patchew.org/QEMU/20190925214948.22212-1-bigeasy@linutronix.de/
def support_clzero():
    if max_extended_function() < 0x80000008: return False
    _, b, _, _ = cpuid.cpuid(0x80000008)
    return (b & (1 << 0)) != 0

#TODO(fernando): por las dudas chequear a ver si la implementación de Golang es correcta!
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


extensions_map = {
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
    73:  support_mwaitx,
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

extensions_names = {
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
    11:  "lzcnt",
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
    73:  "mwaitx",
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

extensions_flags = {
    0:   ["-m32", "-m64"],
    1:   "-mmovbe",
    2:   "-mmmx",
    3:   "-msse",
    4:   "-msse2",
    5:   "-msse3",
    6:   "-mssse3",
    7:   "-msse4.1",
    8:   "-msse4.2",
    9:   "-msse4a",
    10:  "-mpopcnt",
    11:  "-mlzcnt",
    12:  "-mpku",
    13:  "-mavx",
    14:  "-mavx2",
    15:  "-maes",
    16:  "-mpclmul",
    17:  "-mfsgsbase",
    18:  "-mrdrnd",
    19:  "-mfma",
    20:  "-mfma4",
    21:  "-mabm",
    22:  "-mbmi",
    23:  "-mbmi2",
    24:  "-mtbm",
    25:  "-mf16c",
    26:  "-mrdseed",
    27:  "-madx",
    28:  "-mprefetchw",
    29:  "-mclflushopt",
    30:  "-mxsave",
    31:  "-mxsaveopt",
    32:  "-mxsavec",
    33:  "-mxsaves",

    34:  "-mavx512f",
    35:  "-mavx512pf",
    36:  "-mavx512er",
    37:  "-mavx512vl",
    38:  "-mavx512bw",
    39:  "-mavx512dq",
    40:  "-mavx512cd",
    41:  "-mavx5124vnniw",
    42:  "-mavx5124fmaps",
    43:  "-mavx512vbmi",
    44:  "-mavx512ifma",
    45:  "-mavx512vbmi2",
    46:  "-mavx512vpopcntdq",
    47:  "-mavx512bitalg",
    48:  "-mavx512vnni",
    49:  "-mavx512bf16",
    50:  "-mavx512vp2intersect",

    51:  "-msha",
    52:  "-mclwb",
    53:  "-menclv",
    54:  "-mumip",
    55:  "-mptwrite",
    56:  "-mrdpid",
    57:  "-msgx",
    58:  "-mgfni",
    59:  "-mgfni",                      # gfni_sse
    60:  "-mvpclmulqdq",
    61:  "-mvaes",
    62:  "-mpconfig",
    63:  "-mwbnoinvd",
    64:  "-mmovdiri",                   # mmovdir
    65:  "-mmovdir64b",
    66:  "-mbfloat16",
    67:  "-m3dnow",
    68:  "-m3dnowa",                    # 3dnowext
    69:  "-m3dnowprefetch",
    70:  "-mxop",
    71:  "-mlwp",
    72:  "-mcx16",
    73:  "-mmwaitx",
    74:  "-mclzero",
    75:  "-mmmxext",
    76:  "-mprefetchwt1",
}

extensions_compiler_compat = {
    0:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"64 bits",
    1:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"movbe",
    2:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"mmx",
    3:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sse",
    4:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sse2",
    5:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sse3",
    6:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"ssse3",
    7:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sse41",
    8:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sse42",
    9:   {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sse4a",
    10:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"popcnt",
    11:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"lzcnt",
    12:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"pku",
    13:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx",
    14:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx2",
    15:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"aes",
    16:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"pclmul",
    17:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"fsgsbase",
    18:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"rdrnd",
    19:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"fma3",
    20:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"fma4",
    21:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"abm",
    22:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"bmi",
    23:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"bmi2",
    24:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"tbm",
    25:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"f16c",
    26:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"rdseed",
    27:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"adx",
    28:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"prefetchw",
    29:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"clflushopt",
    30:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"xsave",
    31:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"xsaveopt",
    32:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"xsavec",
    33:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"xsaves",

    34:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512f",
    35:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512pf",
    36:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512er",
    37:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512vl",
    38:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512bw",
    39:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512dq",
    40:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512cd",
    41:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx5124vnniw",
    42:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx5124fmaps",
    43:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512vbmi",
    44:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512ifma",
    45:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512vbmi2",
    46:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512vpopcntdq",
    47:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512bitalg",
    48:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512vnni",
    49:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512bf16",
    50:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"avx512vp2intersect",

    51:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sha",
    52:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"clwb",
    53:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"enclv",
    54:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"umip",
    55:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"ptwrite",
    56:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"rdpid",
    57:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"sgx",
    58:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"gfni",
    59:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"gfni_sse",
    60:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"vpclmulqdq",
    61:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"vaes",
    62:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"pconfig",
    63:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"wbnoinvd",
    64:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"movdir",
    65:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"movdir64b",
    66:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"bfloat16",
    67:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"3dnow",
    68:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"3dnowext",
    69:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"3dnowprefetch",
    70:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"xop",
    71:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"lwp",
    72:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"cx16",
    73:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"mwaitx",
    74:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"clzero",
    75:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"mmxext",
    76:  {'gcc':4,'apple-clang': 10,'clang': 10,'msvc': 10,'mingw': 10}, #"prefetchwt1",
}

def get_available_extensions():
    data = []
    for _, f in extensions_map.items():
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
    if len(data) >= len(extensions_map): return data
    n = len(extensions_map) - len(data)
    for i in range(n):
        data.append(int(0))
    return data

def encode_extensions(exts):
    exts = _to_chars_bin(exts)
    exts_str = ''.join(reversed(exts))
    exts_num = int(exts_str, 2)
    exts_num_b58 = base58.flex_encode(exts_num)
    return exts_num_b58

def decode_extensions(architecture_id):
    exts_num = base58.flex_decode(architecture_id)
    res = "{0:b}".format(exts_num)
    res = res.zfill(len(extensions_map))
    return _to_ints_bin([*reversed(res)])
    # return [*reversed(res)]

def get_architecture_id():
    exts = get_available_extensions()
    architecture_id = encode_extensions(exts)
    return architecture_id

def print_available_extensions(exts):
    for i in range(len(exts)):
        if (exts[i] == 1):
            print("your computer supports " + extensions_names[i])

# ----------------------------------------------------------------------

class Vendor(Enum):
    Other = 0,
    Intel = 1,
    AMD = 2,
    VIA = 3,
    Transmeta = 4,
    NSC = 5,
    KVM = 6,         # Kernel-based Virtual Machine
    MSVM = 7,        # Microsoft Hyper-V or Windows Virtual PC
    VMware = 8,
    XenHVM = 9,
    Bhyve = 10,
    Hygon = 11,


# Except from http://en.wikipedia.org/wiki/CPUID#EAX.3D0:_Get_vendor_ID
vendorMapping = {
	"AMDisbetter!": Vendor.AMD,
	"AuthenticAMD": Vendor.AMD,
	"CentaurHauls": Vendor.VIA,
	"GenuineIntel": Vendor.Intel,
	"TransmetaCPU": Vendor.Transmeta,
	"GenuineTMx86": Vendor.Transmeta,
	"Geode by NSC": Vendor.NSC,
	"VIA VIA VIA ": Vendor.VIA,
	"KVMKVMKVMKVM": Vendor.KVM,
	"Microsoft Hv": Vendor.MSVM,
	"VMwareVMware": Vendor.VMware,
	"XenVMMXenVMM": Vendor.XenHVM,
	"bhyve bhyve ": Vendor.Bhyve,
	"HygonGenuine": Vendor.Hygon,
}

def vendorID():
    v = cpuid.cpu_vendor()
    vend = vendorMapping.get(v, Vendor.Other)
    return vend

def brandName():
    if max_extended_function() >= 0x80000004:
        return cpuid.cpu_name()
    return "unknown"

def cacheLine():
	if max_function_id() < 0x1:
		return 0

	_, ebx, _, _ = cpuid.cpuid(1)
	cache = (ebx & 0xff00) >> 5 # cflush size
	if cache == 0 and max_extended_function() >= 0x80000006:
		_, _, ecx, _ = cpuid.cpuid(0x80000006)
		cache = ecx & 0xff # cacheline size
	#TODO: Read from Cache and TLB Information
	return int(cache)

def familyModel():
	if max_function_id() < 0x1:
		return 0, 0
	eax, _, _, _ = cpuid.cpuid(1)
	family = ((eax >> 8) & 0xf) + ((eax >> 20) & 0xff)
	model = ((eax >> 4) & 0xf) + ((eax >> 12) & 0xf0)
	return int(family), int(model)

def threadsPerCore():
	mfi = max_function_id()
	if mfi < 0x4 or vendorID() != Vendor.Intel:
		return 1

	if mfi < 0xb:
		_, b, _, d = cpuid.cpuid(1)
		if (d & (1 << 28)) != 0:
			# v will contain logical core count
			v = (b >> 16) & 255
			if v > 1:
				a4, _, _, _ = cpuid.cpuid(4)
				# physical cores
				v2 = (a4 >> 26) + 1
				if v2 > 0:
					return int(v) / int(v2)
		return 1
	_, b, _, _ = cpuid.cpuid_count(0xb, 0)
	if b&0xffff == 0:
		return 1
	return int(b & 0xffff)


def logicalCores():
    mfi = max_function_id()
    vend = vendorID()
	
    if vend == Vendor.Intel:
        # Use this on old Intel processors
        if mfi < 0xb:
            if mfi < 1:
                return 0
            # CPUID.1:EBX[23:16] represents the maximum number of addressable IDs (initial APIC ID)
            # that can be assigned to logical processors in a physical package.
            # The value may not be the same as the number of logical processors that are present in the hardware of a physical package.
            _, ebx, _, _ = cpuid.cpuid(1)
            logical = (ebx >> 16) & 0xff
            return int(logical)
        _, b, _, _ = cpuid.cpuid_count(0xb, 1)
        return int(b & 0xffff)
    elif vend == Vendor.AMD or vend == Vendor.Hygon:
        _, b, _, _ = cpuid.cpuid(1)
        return int((b >> 16) & 0xff)
    else:
        return 0
	
def physicalCores():
    vend = vendorID()
	
    if vend == Vendor.Intel:
        return logicalCores() / threadsPerCore()
    elif vend == Vendor.AMD or vend == Vendor.Hygon:
        if max_extended_function() >= 0x80000008:
            _, _, c, _ = cpuid.cpuid(0x80000008)
            return int(c&0xff) + 1
    return 0


def support_rdtscp():
    if max_extended_function() < 0x80000001: return False
    _, _, _, d = cpuid.cpuid(0x80000001)
    return (d & (1 << 27)) != 0

#TODO(fernando): implementar RTCounter() del proyecto Golang
#TODO(fernando): implementar Ia32TscAux() del proyecto Golang

# LogicalCPU will return the Logical CPU the code is currently executing on.
# This is likely to change when the OS re-schedules the running thread
# to another CPU.
# If the current core cannot be detected, -1 will be returned.
def LogicalCPU():
    if max_function_id() < 1:
        return -1
    _, ebx, _, _ = cpuid.cpuid(1)
    return int(ebx >> 24)


# VM Will return true if the cpu id indicates we are in
# a virtual machine. This is only a hint, and will very likely
# have many false negatives.
def VM():
    vend = vendorID()
    if vend == Vendor.MSVM or vend == Vendor.KVM or vend == Vendor.VMware or vend == Vendor.XenHVM or vend == Vendor.Bhyve:
        return True
    return False

def Hyperthreading():
    if max_function_id() < 4: return False
    _, _, _, d = cpuid.cpuid(1)
    if vendorID() == Vendor.Intel and (d&(1<<28)) != 0:
        if threadsPerCore() > 1:
            return True
    return False


# ----------------------------------------------------------------------

def is_superset_of(a, b):
    n = min(len(a), len(b))

    for i in range(n):
        if a[i] < b[i]: return False

    for i in range(n, len(b)):
        if b[i] == 1: return False

    return True

def test_is_superset_of():
    assert(is_superset_of([], []))
    assert(is_superset_of([0], []))
    assert(is_superset_of([], [0]))
    assert(is_superset_of([0], [0]))
    assert(is_superset_of([0,0], [0,0]))
    assert(is_superset_of([0], [0,0]))
    assert(is_superset_of([0,0], [0]))
    assert(is_superset_of([1], [1]))
    assert(is_superset_of([1], [0]))
    assert(is_superset_of([1], []))

    assert(not is_superset_of([0], [1]))
    assert(not is_superset_of([], [1]))

test_is_superset_of()
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------


# intel_marchs = {
#     'i386':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'i486':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'i586':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'lakemont':       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'pentium-mmx':    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'pentiumpro':     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'i686':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'pentium2':       [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'pentium3':       [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'pentium-m':      [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'pentium4':       [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'prescott':       [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'x86-64':         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'nocona':         [1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'core2':          [1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'nehalem':        [1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'westmere':       [1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'sandybridge':    [1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'ivybridge':      [1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?],
#     'haswell':        [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,?,?],
#     'broadwell':      [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,1,?,?,?,?],
#     'skylake':        [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,?,?,?,?],
#     'bonnell':        [1,1,1,1,1,1,1,0,0,0,0,?,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?,?],
#     'silvermont':     [1,1,1,1,1,1,1,1,1,0,1,?,0,0,0,1,1,0,1,0,0,?,0,0,0,0,0,0,0,0,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?,?],
#     'goldmont':       [1,1,1,1,1,1,1,1,1,0,1,?,0,0,0,1,1,1,1,0,0,?,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?,?],
#     'goldmont-plus':  [1,1,1,1,1,1,1,1,1,0,1,?,0,0,0,1,1,1,1,0,0,?,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?,?],
#     'tremont':        [1,1,1,1,1,1,1,1,1,0,1,?,0,0,0,1,1,1,1,0,0,?,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,?,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,?,?,?,?,?,?,?,?],
#     'knl':            [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,?,?,?,?,?],
#     'knm':            [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,?,?,?,?,?],
#     'skylake-avx512': [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,1,?,?,?,?],
#     'cannonlake':     [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,?,?,?,?,?],
#     'icelake-client': [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,?,?,1,?,?,?,?],
#     'icelake-server': [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,?,?,1,?,?,?,?],
#     'cascadelake':    [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,?,?,?,?,?,?,?],
#     'cooperlake':     [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,?,?,?,?,?,?,?],
#     'tigerlake':      [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,?,?,1,?,?,?,?],
#     'alderlake':      [],
#     'meteor_lake':    [],
# }


intel_marchs = {
    'i386':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'i486':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'i586':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'lakemont':       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'pentium-mmx':    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'pentiumpro':     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'i686':           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'pentium2':       [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'pentium3':       [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'pentium-m':      [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'pentium4':       [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'prescott':       [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'x86-64':         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'nocona':         [1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'core2':          [1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'nehalem':        [1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'westmere':       [1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'sandybridge':    [1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'ivybridge':      [1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'haswell':        [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    'broadwell':      [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
    'skylake':        [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
    'bonnell':        [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'silvermont':     [1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'goldmont':       [1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'goldmont-plus':  [1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'tremont':        [1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'knl':            [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    'knm':            [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    'skylake-avx512': [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
    'cannonlake':     [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    'icelake-client': [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
    'icelake-server': [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0],
    'cascadelake':    [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    'cooperlake':     [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
    'tigerlake':      [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0],
    'alderlake':      [],
    'meteor_lake':    [],
}


# ----------------------------------------------------------------------------------


print("vendorID: %s" % vendorID())
print("brandName: %s" % brandName())
print("cacheLine: %s" % cacheLine())
print("familyModel: %s, %s" % familyModel())
print("threadsPerCore: %s" % threadsPerCore())
print("logicalCores: %s" % logicalCores())
print("physicalCores: %s" % physicalCores())
print("LogicalCPU: %s" % LogicalCPU())
print("VM: %s" % VM())
print("Hyperthreading: %s" % Hyperthreading())

print("CPUID Microarchitecture : %s%s" % cpuid.cpu_microarchitecture())
architecture_id = get_architecture_id()
print(architecture_id)


# ----------------------------------------------------------------------------------

# architecture_id = encode_extensions(exts)

for name, exts in intel_marchs.items():
    if len(exts) > 0:
        print('%s: %s' % (name, encode_extensions(exts)))

# ----------------------------------------------------------------------------------


# # According XLS
# haswell = [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
# haswell = _pad_right_array(haswell)

# skylake = [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]
# skylake = _pad_right_array(skylake)

# comparable_arch = skylake

# if is_superset_of(skylake, haswell):
#     print("Skylake is a superset of Haswell")
# else:
#     print("Skylake is NOT a superset of Haswell")



# # print(comparable_arch)

# # print_available_extensions(comparable_arch)

# exts = get_available_extensions()
# print(exts)
# print_available_extensions(exts)

# print("---------------------------------------------")
# print(support_avx_os())
# print(support_avx2_cpu())
# print("---------------------------------------------")


# for i in range(len(exts)):
#     if exts[i] != comparable_arch[i]:
#         print("difference in pos " + str(i) + "    " + extensions_names[i])
#         if exts[i] == 0:
#             print("XLS supports    " + extensions_names[i])
#         else:
#             print("CPU supports    " + extensions_names[i])






#                                                        X        X              X  X                    X  X                                                                                                                          X  X                 
# haswell xls [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# calculated  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# architecture_id = encode_extensions(exts)
# print(architecture_id)
# print(decode_extensions(architecture_id))




# data_str = ''.join(reversed(data))
# print(data_str)
# data_num = int(data_str, 2)
# print(data_num)
# print(hex(data_num))

# data_num_b58 = base58.flex_encode(data_num)
# print(data_num_b58)
# x_dec = base58.flex_decode(data_num_b58)
# print(x_dec)



# 0x80000000000c22dadff

# print(base64.b64encode(bytes([data_num])))
# print(base64.b64encode(bytes(data2)))

# data = ['0' for _ in range(256)]
# print(data)

# print("".join(data))


# print(extensions[0]())
# print(extensions_map[1]())
# print(extensions_map[2]())
# print(extensions_map[9]())
# print(extensions_map[13]())
# # print(extensions_map[75]())
# print(extensions_map[76]())



# print(support_xsave_cpu())
# print(support_osxsave())
# print(support_xsaveopt_cpu())






# machdep.cpu.signature: 263777
# machdep.cpu.brand: 0
# machdep.cpu.features: 

# FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH 
# DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX SMX 
# EST TM2 SSSE3 FMA CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC MOVBE POPCNT AES PCID 
# XSAVE OSXSAVE SEGLIM64 TSCTMR AVX1.0 RDRAND F16C

# machdep.cpu.leaf7_features: 

# RDWRFSGS TSC_THREAD_OFFSET BMI1 AVX2 SMEP BMI2 ERMS INVPCID FPU_CSDS MDCLEAR 
# IBRS STIBP L1DF SSBD

# machdep.cpu.extfeatures: 

# SYSCALL XD 1GBPAGE EM64T LAHF LZCNT RDTSCP TSCI

# machdep.cpu.logical_per_package: 16
# machdep.cpu.cores_per_package: 8
# machdep.cpu.microcode_version: 27
# machdep.cpu.processor_flag: 5
# machdep.cpu.mwait.linesize_min: 64
# machdep.cpu.mwait.linesize_max: 64