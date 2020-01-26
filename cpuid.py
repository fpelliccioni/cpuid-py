import struct
import cpuid_native

def cpuid(leaf):
    _, a, b, c, d = cpuid_native.get_cpuid(leaf)
    return (a, b, c, d)

def cpuid_count(leaf, subleaf):
    _, a, b, c, d = cpuid_native.get_cpuid_count(leaf, subleaf)
    return (a, b, c, d)

def cpu_vendor():
    _, b, c, d = cpuid(0)
    return struct.pack("III", b, d, c).decode("utf-8")

def cpu_name():
    return "".join((struct.pack("IIII", *cpuid(0x80000000 + i)).decode("utf-8")
                    for i in range(2, 5))).strip()

def xgetbv(ctr):
    return cpuid_native.xgetbv(ctr)

def _is_set(id, reg_idx, bit):
    regs = cpuid(id)

    if (1 << bit) & regs[reg_idx]:
        return "Yes"
    else:
        return "--"

def _is_bmi2(b):
    # (feature_string[0 + 8 / 8] & (1 << (8 % 8))) == 0
    bit_BMI2 = 0x00000100
    return b & bit_BMI2 != 0

def _is_bmi2_cpuid():
    _, b, _, _ = cpuid_count(7, 0)
    return _is_bmi2(b)

def _is_osxsave(c):
    # cpuid_osxsave = (feature_string[11] >> 3) & 1;
    bit_OSXSAVE = 0x08000000        # (1 << 27)
    return c & bit_OSXSAVE != 0

def _is_osxsave_cpuid():
    _, _, c, _ = cpuid(1)
    return _is_osxsave(c)

def _is_avx(c):
    # cpuid_avx     = (feature_string[11] >> 4) & 1;
    bit_AVX = 0x10000000            # (1 << 28)
    return c & bit_AVX != 0

def _is_avx_cpuid():
    _, _, c, _ = cpuid(1)
    return _is_avx(c)

def _is_long_mode(d):
#   CPUID (feature_string, 0x80000001);
#   cpuid_64bit = (feature_string[7] >> 5) & 1;
    bit_LM = 0x20000000            # (1 << 29)
    return d & bit_LM != 0

def _is_long_mode_cpuid():
    _, _, _, d = cpuid(0x80000001)
    return _is_long_mode(d)

# https://en.wikichip.org/wiki/intel/cpuid
def _intel(family, model):
    cpu_64bit = 0
    cpu_avx = 0
    modelstr = ""
    
    if family == 5:
        if model <= 2:
            modelstr = "pentium"
        elif model >= 4:
            modelstr = "pentiummmx"
    elif family == 6:
        if model <= 1:
            modelstr = "pentiumpro"
        elif model <= 6:
            modelstr = "pentium2"
        elif model <= 8:
            modelstr = "pentium3"
        elif model <= 9:
            modelstr = "pentiumm"
        elif model <= 0x0c:
            modelstr = "pentium3"
        elif model <= 0x0e:
            modelstr = "pentiumm"
        elif model <= 0x19:
            cpu_64bit = 1
            modelstr = "core2"
        elif model == 0x1a:
            cpu_64bit = 1
            modelstr = "nehalem"    # NHM Gainestown */
        elif model == 0x1c:
            cpu_64bit = 1
            modelstr = "atom"       # Silverthorne */
        elif model == 0x1d:
            cpu_64bit = 1
            modelstr = "core2"      # PNR Dunnington */
        elif model == 0x1e:
            cpu_64bit = 1
            modelstr = "nehalem"    # NHM Lynnfield/Jasper */
        elif model == 0x25:
            cpu_64bit = 1
            modelstr = "westmere"   # WSM Clarkdale/Arrandale */
        elif model == 0x26:
            cpu_64bit = 1
            modelstr = "atom"       # Lincroft */
        elif model == 0x27:
            cpu_64bit = 1
            modelstr = "atom"       # Saltwell */
        elif model == 0x2a:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "sandybridge"# SB */
        elif model == 0x2c:
            cpu_64bit = 1
            modelstr = "westmere"   # WSM Gulftown */
        elif model == 0x2d:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "sandybridge"# SBC-EP */
        elif model == 0x2e:
            cpu_64bit = 1
            modelstr = "nehalem"    # NHM Beckton */
        elif model == 0x2f:
            cpu_64bit = 1
            modelstr = "westmere"   # WSM Eagleton */
        elif model == 0x36:
            cpu_64bit = 1
            modelstr = "atom"       # Cedarview/Saltwell */
        elif model == 0x37:
            cpu_64bit = 1
            modelstr = "silvermont" # Silvermont */
        elif model == 0x3a:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "ivybridge"  # IBR */
        elif model == 0x3c:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "haswell"    # Haswell client */
        elif model == 0x3d:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "broadwell"  # Broadwell */
        elif model == 0x3e:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "ivybridge"  # Ivytown */
        elif model == 0x3f:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "haswell"    # Haswell server */
        elif model == 0x45:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "haswell"    # Haswell ULT */
        elif model == 0x46:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "haswell"    # Crystal Well */
        elif model == 0x47:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "broadwell"  # Broadwell */
        elif model == 0x4a:
            cpu_64bit = 1
            modelstr = "silvermont" # Silvermont */
        elif model == 0x4c:
            cpu_64bit = 1
            modelstr = "silvermont" # Airmont */
        elif model == 0x4d:
            cpu_64bit = 1
            modelstr = "silvermont" # Silvermont/Avoton */
        elif model == 0x4e:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "skylake"    # Skylake client */
        elif model == 0x4f:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "broadwell"  # Broadwell server */
        elif model == 0x55:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "skylake-avx512"    # Skylake server */
        elif model == 0x56:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "broadwell"  # Broadwell microserver */
        elif model == 0x57:
            cpu_64bit = 1
            modelstr = "knightslanding" # aka Xeon Phi */
        elif model == 0x5a:
            cpu_64bit = 1
            modelstr = "silvermont" # Silvermont */
        elif model == 0x5c:
            cpu_64bit = 1
            modelstr = "goldmont"   # Goldmont */
        elif model == 0x5e:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "skylake"    # Skylake */
        elif model == 0x5f:
            cpu_64bit = 1
            modelstr = "goldmont"   # Goldmont */
        elif model == 0x8e:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "kabylake"   # Kabylake Y/U */
        elif model == 0x9e:
            cpu_64bit = 1
            cpu_avx=1
            modelstr = "kabylake"   # Kabylake desktop */
        else:
            cpu_64bit = 1
            modelstr = "nehalem"    # default */

        if modelstr == "haswell" or modelstr == "broadwell" or modelstr == "skylake":
            # Some haswell, broadwell, skylake lack BMI2.  Let them appear as sandybridge for now.

            if not _is_bmi2_cpuid() or _workaround_skylake_cpuid_bug():
                modelstr = "sandybridge"
    elif family == 15:
        cpu_64bit = 1
        modelstr = "pentium4"

    return modelstr, cpu_64bit, cpu_avx


def _amd(family, model):
    cpu_64bit = 0
    cpu_avx = 0
    modelstr = ""

    if family == 5:
        if model <= 3:
            modelstr = "k5"
        elif model <= 7:
            modelstr = "k6"
        elif model == 8:
            modelstr = "k62"
        elif model == 9:
            modelstr = "k63"
        elif model == 10:
            modelstr = "geode"
        elif model == 13:
            modelstr = "k63"
    elif family == 6:
        modelstr = "athlon"
    elif family == 15:		# K8, K9
        cpu_64bit = 1
        modelstr = "k8"
    elif family == 16:		# K10
        cpu_64bit = 1
        modelstr = "k10"
    elif family == 17:		# Hybrid k8/k10, claim k8
        cpu_64bit = 1
        modelstr = "k8"
    elif family == 18:		# Llano, uses K10 core
        cpu_64bit = 1
        modelstr = "k10"
    elif family == 19:		# AMD Internal, assume future K10
        cpu_64bit = 1
        modelstr = "k10"
    elif family == 20:		# Bobcat
        cpu_64bit = 1
        modelstr = "bobcat"
    elif family == 21:		# Bulldozer
        cpu_64bit = 1
        cpu_avx = 1
        if model <= 1:
            modelstr = "bulldozer"
        elif model < 0x20:	# really 2, [0x10-0x20)
            modelstr = "piledriver"
        elif model < 0x40:	# really [0x30-0x40)
            modelstr = "steamroller"
        else:				# really [0x60-0x70)
            modelstr = "excavator"
    elif family == 22:		# Jaguar, an improved bobcat
        cpu_64bit = 1
        cpu_avx = 1
        modelstr = "jaguar"

    return modelstr, cpu_64bit, cpu_avx


def _centaur_hauls(family, model):
    cpu_64bit = 0
    cpu_avx = 0
    modelstr = ""

    if family == 6:
        if model < 9:
            modelstr = "viac3"
        elif model < 15:
            modelstr = "viac32"
        else:
            cpu_64bit = 1
            modelstr = "nano"

    return modelstr, cpu_64bit, cpu_avx


def _workaround_skylake_cpuid_bug():
    # Example strings:
    # "Intel(R) Pentium(R) CPU G4400 @ 3.30GHz"
    # "Intel(R) Core(TM) i5-6600K CPU @ 3.50GHz"
    #                  ^               ^               ^
    #     0x80000002       0x80000003      0x80000004
    # We match out just the 0x80000003 part here.

    # In their infinitive wisdom, Intel decided to use one register order for
    #   the vendor string, and another for the processor name string.  We shuffle
    #   things about here, rather than write a new variant of our assembly cpuid.

    bad_cpus = [" G44", " G45", " G39" ]
    processor_name_string = struct.pack("IIII", *cpuid(0x80000003)).decode("utf-8")

    for bad in bad_cpus:
        if bad in processor_name_string:
            return True

    return False


def cpu_microarchitecture():

    fms, b, c, d = cpuid(1)
    family = ((fms >> 8) & 0xf) + ((fms >> 20) & 0xff)
    model = ((fms >> 4) & 0xf) + ((fms >> 12) & 0xf0)

    vendor_string = cpu_vendor()
    if vendor_string == "GenuineIntel":
        modelstr, cpu_64bit, cpu_avx = _intel(family, model)
    elif vendor_string == "AuthenticAMD":
        modelstr, cpu_64bit, cpu_avx = _amd(family, model)
    # elif vendor_string == "CyrixInstead":
    #     #TODO(bitprim): Should recognize Cyrix' processors too.
    elif vendor_string == "CentaurHauls":
        modelstr, cpu_64bit, cpu_avx = _centaur_hauls(family, model)

    cpuid_64bit = _is_long_mode_cpuid()

    suffix = ''

    if cpuid_64bit and not cpu_64bit:
        # If our cpuid-based CPU identification thinks this is a 32-bit CPU but
        #   cpuid claims AMD64 capabilities, then revert to the generic "x86_64".
        #   This is of course wrong, but it can happen in some virtualisers and
        #   emulators, and this workaround allows for successful 64-bit builds.
        modelstr = "x86_64"
    elif cpu_avx and not (_is_avx(c) and _is_osxsave(c)):
        #  For CPUs nominally capable of executing AVX, append "noavx" when not
        #   both the AVX and OSXSAVE cpuid bits are set.  We tolerate weirdness
        #   here, as some virtualisers set a broken cpuid state here, while other
        #   virtualisers allow users to set a broken state.  
        suffix = "noavx"

    # print("%s%s" % (modelstr, suffix))
    return (modelstr, suffix)



if __name__ == "__main__":
    
    print("Vendor ID         : %s" % cpu_vendor())
    print("CPU name          : %s" % cpu_name())
    print("Microarchitecture : %s%s" % cpu_microarchitecture())
    print("Vector instructions supported:")
    print("SSE       : %s" % is_set(1, 3, 25))
    print("SSE2      : %s" % is_set(1, 3, 26))
    print("SSE3      : %s" % is_set(1, 2, 0))
    print("SSSE3     : %s" % is_set(1, 2, 9))
    print("SSE4.1    : %s" % is_set(1, 2, 19))
    print("SSE4.2    : %s" % is_set(1, 2, 20))
    print("SSE4a     : %s" % is_set(0x80000001, 2, 6))
    print("AVX       : %s" % is_set(1, 2, 28))
    print("AVX2      : %s" % is_set(7, 1, 5))
    print("BMI1      : %s" % is_set(7, 1, 3))
    print("BMI2      : %s" % is_set(7, 1, 8))

