# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           coin-or-cgl
Version:        0.60.10
Release:        %autorelease
Summary:        Cut generators for COIN-OR integer programming solvers
License:        EPL-2.0
URL:            https://github.com/coin-or/Cgl
#!RemoteAsset:  sha256:41b7ac9402db883d9c487eb7101e59eb513cefd726e6e7a669dc94664d9385e6
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Cgl-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n Cgl-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(osi-clp)

%description
Cgl generates cutting planes used by COIN-OR solvers to tighten linear
relaxations of mixed-integer problems.

%package        devel
Summary:        Development files for Cgl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Cgl.

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

%check -a
# The upstream unitTest opens MIPLIB p0033 and other externally supplied models.
# Exercise a fractional relaxation with a known integer optimum in the buildroot.
cat >check-gomory.cpp <<'TEST'
#include <coin/CglGomory.hpp>
#include <coin/OsiClpSolverInterface.hpp>
#include <coin/CoinPackedMatrix.hpp>
#include <coin/CoinPackedVector.hpp>
#include <cmath>
int main() {
    OsiClpSolverInterface solver;
    CoinPackedMatrix matrix(false, 0, 0);
    matrix.setDimensions(0, 2);
    CoinPackedVector constraint;
    constraint.insert(0, 2); constraint.insert(1, 2);
    matrix.appendRow(constraint);
    const double lo[] = {0, 0}, hi[] = {1, 1}, cost[] = {-1, -1};
    const double lhs[] = {-solver.getInfinity()}, rhs[] = {3};
    solver.loadProblem(matrix, lo, hi, cost, lhs, rhs);
    solver.setInteger(0); solver.setInteger(1);
    solver.initialSolve();
    if (std::abs(solver.getObjValue() + 1.5) > 1e-8) return 1;
    CglGomory gomory;
    OsiCuts cuts;
    gomory.generateCuts(solver, cuts);
    if (!cuts.sizeRowCuts() && !cuts.sizeColCuts()) return 2;
    solver.applyCuts(cuts);
    solver.resolve();
    return !solver.isProvenOptimal() || std::abs(solver.getObjValue() + 1.0) > 1e-8;
}
TEST
%{__cxx} %{build_cxxflags} -I%{buildroot}%{_includedir} $(pkg-config --cflags osi-clp) check-gomory.cpp \
    %{build_ldflags} -L%{buildroot}%{_libdir} -lCgl $(pkg-config --libs osi-clp) -o check-gomory
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./check-gomory

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libCgl.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libCgl.so
%{_libdir}/pkgconfig/cgl.pc
%{_datadir}/coin/doc/Cgl/

%changelog
%autochangelog
