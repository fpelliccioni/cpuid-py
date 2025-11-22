# cpuid

[![PyPI version](https://badge.fury.io/py/cpuid.svg)](https://badge.fury.io/py/cpuid)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Support](https://img.shields.io/pypi/pyversions/cpuid.svg)](https://pypi.org/project/cpuid/)

**High-level Pythonic API for x86 CPU identification and feature detection**

A user-friendly Python library that automatically identifies your CPU vendor, model, microarchitecture, and supported instruction sets. Built on top of [cpuid-native](https://github.com/fpelliccioni/cpuid-py-native) for direct hardware access.

## Features

- **Automatic CPU identification** - Detects Intel, AMD, and VIA processors
- **Microarchitecture detection** - Identifies specific CPU generations (Sandy Bridge, Haswell, Zen, etc.)
- **Instruction set detection** - Checks support for SSE, AVX, AVX2, BMI, and more
- **Zero configuration** - Just import and use
- **Cross-platform** - Linux, macOS, and Windows support
- **Python 3.7+** - Full support through Python 3.13

## Installation

```bash
pip install cpuid
```

## Quick Start

```python
import cpuid

# Get CPU vendor
vendor = cpuid.cpu_vendor()
print(f"Vendor: {vendor}")  # e.g., "GenuineIntel" or "AuthenticAMD"

# Get CPU name/brand
name = cpuid.cpu_name()
print(f"CPU: {name}")  # e.g., "Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz"

# Detect microarchitecture
arch, suffix = cpuid.cpu_microarchitecture()
print(f"Microarchitecture: {arch}{suffix}")  # e.g., "kabylake" or "zen2"

# Check for specific instruction sets
eax, ebx, ecx, edx = cpuid.cpuid(1)
has_sse2 = bool(edx & (1 << 26))
has_avx = bool(ecx & (1 << 28))
print(f"SSE2: {has_sse2}, AVX: {has_avx}")
```

## Real-World Example

```python
import cpuid

def detect_cpu_capabilities():
    """Detect CPU and print comprehensive information."""

    vendor = cpuid.cpu_vendor()
    name = cpuid.cpu_name()
    arch, suffix = cpuid.cpu_microarchitecture()

    print("=" * 60)
    print(f"Vendor: {vendor}")
    print(f"Model:  {name}")
    print(f"Arch:   {arch}{suffix}")
    print("=" * 60)

    # Check vector instruction support
    _, _, ecx, edx = cpuid.cpuid(1)

    features = {
        "SSE": bool(edx & (1 << 25)),
        "SSE2": bool(edx & (1 << 26)),
        "SSE3": bool(ecx & (1 << 0)),
        "SSSE3": bool(ecx & (1 << 9)),
        "SSE4.1": bool(ecx & (1 << 19)),
        "SSE4.2": bool(ecx & (1 << 20)),
        "AVX": bool(ecx & (1 << 28)),
    }

    # Check AVX2 and BMI
    _, ebx, _, _ = cpuid.cpuid_count(7, 0)
    features["AVX2"] = bool(ebx & (1 << 5))
    features["BMI1"] = bool(ebx & (1 << 3))
    features["BMI2"] = bool(ebx & (1 << 8))

    print("\nVector Instructions:")
    for name, supported in features.items():
        status = "✓" if supported else "✗"
        print(f"  {status} {name}")

if __name__ == "__main__":
    detect_cpu_capabilities()
```

Output example:
```
============================================================
Vendor: GenuineIntel
Model:  Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
Arch:   kabylake
============================================================

Vector Instructions:
  ✓ SSE
  ✓ SSE2
  ✓ SSE3
  ✓ SSSE3
  ✓ SSE4.1
  ✓ SSE4.2
  ✓ AVX
  ✓ AVX2
  ✓ BMI1
  ✓ BMI2
```

## API Reference

### High-Level Functions

#### `cpu_vendor() -> str`
Returns the CPU vendor string (e.g., `"GenuineIntel"`, `"AuthenticAMD"`, `"CentaurHauls"`).

#### `cpu_name() -> str`
Returns the full CPU brand string (e.g., `"Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz"`).

#### `cpu_microarchitecture() -> Tuple[str, str]`
Returns a tuple of `(architecture, suffix)` where:
- `architecture`: Detected microarchitecture (e.g., `"haswell"`, `"skylake"`, `"zen2"`)
- `suffix`: Additional flags like `"noavx"` if AVX is disabled

**Intel architectures:** `pentium`, `pentium2`, `pentium3`, `pentium4`, `core2`, `nehalem`, `westmere`, `sandybridge`, `ivybridge`, `haswell`, `broadwell`, `skylake`, `kabylake`, `atom`, `silvermont`, `goldmont`

**AMD architectures:** `k5`, `k6`, `athlon`, `k8`, `k10`, `bobcat`, `bulldozer`, `piledriver`, `steamroller`, `excavator`, `jaguar`

### Low-Level Functions

#### `cpuid(leaf: int) -> Tuple[int, int, int, int]`
Executes CPUID instruction and returns `(eax, ebx, ecx, edx)` register values.

#### `cpuid_count(leaf: int, subleaf: int) -> Tuple[int, int, int, int]`
Executes CPUID with both leaf and subleaf, returns `(eax, ebx, ecx, edx)`.

#### `xgetbv(ctr: int) -> int`
Reads extended control register (typically `ctr=0` for XCR0).

## Supported Architectures

### Intel
- **Legacy:** Pentium, Pentium MMX, Pentium Pro, Pentium II/III/4, Pentium M
- **Core:** Core 2, Nehalem, Westmere, Sandy Bridge, Ivy Bridge
- **Modern:** Haswell, Broadwell, Skylake, Kaby Lake, Coffee Lake
- **Low-power:** Atom, Silvermont, Goldmont
- **HPC:** Knights Landing (Xeon Phi)

### AMD
- **Legacy:** K5, K6, Athlon
- **64-bit:** K8, K10
- **Bulldozer family:** Bulldozer, Piledriver, Steamroller, Excavator
- **Modern:** Bobcat, Jaguar, Zen (through microarchitecture detection)

### VIA
- C3, C7, Nano

## Use Cases

- **Performance optimization** - Select optimal algorithms based on CPU features
- **System requirements** - Check if CPU supports required instruction sets
- **Benchmarking** - Categorize results by CPU architecture
- **Cross-platform development** - Adapt code paths for different CPUs
- **System monitoring** - Display detailed CPU information

## Low-Level Access

Need direct access to CPUID registers? Use [cpuid-native](https://github.com/fpelliccioni/cpuid-py-native):

```python
import cpuid_native

success, eax, ebx, ecx, edx = cpuid_native.get_cpuid(1)
tsc, aux = cpuid_native.rdtscp()
xcr0 = cpuid_native.xgetbv(0)
```

## Building from Source

```bash
git clone https://github.com/fpelliccioni/cpuid-py.git
cd cpuid-py
pip install -e .
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

Created and maintained by [Fernando Pelliccioni](https://github.com/fpelliccioni)
