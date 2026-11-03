# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clucene
Version:        2.3.3.4
Release:        %autorelease
Summary:        C++ full-text indexing and search library
License:        LGPL-2.1-or-later OR Apache-2.0
URL:            https://sourceforge.net/projects/clucene/
VCS:            git:https://git.code.sf.net/p/clucene/code
#!RemoteAsset:  sha256:ddfdc433dd8ad31b5c5819cc4404a8d2127472a3b720d3e744e8c51d79732eab
Source0:        https://downloads.sourceforge.net/project/clucene/clucene-core-unstable/2.3/clucene-core-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(prep):  -n clucene-core-%{version}
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DBUILD_CONTRIBS_LIB=ON
BuildOption(conf):  -DLIB_SUFFIX=64
BuildOption(conf):  -DLUCENE_SYS_INCLUDES=%{_includedir}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

%patchlist
# Downstream patch for missing gmtime and strftime declarations in 2.3.3.4.
# https://sourceforge.net/p/clucene/code/ci/clucene-src-2.3.3.4/tree/src/core/CLucene/document/DateTools.cpp
2000-include-time-declarations-in-DateTools.patch
# Downstream fix for the Linux build with distribution compiler flags.
# https://sourceforge.net/p/clucene/code/ci/clucene-src-2.3.3.4/tree/src/test/search/TestIndexSearcher.cpp
2001-include-usleep-declaration-in-search-test.patch
# Downstream fix for tests configured before the contribs library subproject.
# https://sourceforge.net/p/clucene/code/ci/clucene-src-2.3.3.4/tree/src/test/CMakeLists.txt
2002-use-contribs-headers-in-tests.patch
# Downstream fix for escaped range endpoints covered by testEscaped.
# https://sourceforge.net/p/clucene/code/ci/clucene-src-2.3.3.4/tree/src/core/CLucene/queryParser/QueryParser.cpp
2003-copy-overlapping-quoted-range-endpoints-safely.patch
# Submitted by Vitaliy Filippov, CLucene issue 200.
# https://sourceforge.net/p/clucene/bugs/200/
2004-install-the-contribs-library-and-public-headers.patch
# C++ port of the upstream Lucene token-stream correction for LUCENE-973.
# https://github.com/apache/lucene/commit/835c405be09d20f0b174e7ce96bd675e9400c946
2005-stop-after-the-final-cjk-bigram.patch

%description
CLucene implements indexing, tokenization and querying of full-text
search indexes in C++. Its contributed analyzers support multiple
languages and text formats.

%package        devel
Summary:        Development files for CLucene
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and build metadata for C++ applications using CLucene.

%check -p
# Build the CLucene test executable before CTest runs the index and query suite.
cmake --build %{_vpath_builddir} --target cl_test --parallel %{_smp_build_ncpus}

%check -a
# Tokenize Chinese text with the installed interfaces used to build LibreOffice help indexes.
cat >check-cjk.cpp <<'TEST'
#include <CLucene.h>
#include <CLucene/analysis/LanguageBasedAnalyzer.h>
#include <CLucene/analysis/cjk/CJKAnalyzer.h>
#include <clocale>
#include <cwchar>
#include <cstdio>
#include <memory>

int main()
{
    if (!std::setlocale(LC_CTYPE, "C.UTF-8"))
        return 2;
    lucene::analysis::LanguageBasedAnalyzer analyzer(L"cjk");
    lucene::util::StringReader text(L"中文索引");
    std::unique_ptr<lucene::analysis::TokenStream> tokens(analyzer.tokenStream(L"contents", &text));
    lucene::analysis::Token token;
    for (const wchar_t* expected : { L"中文", L"文索", L"索引" }) {
        const auto* result = tokens->next(&token);
        if (!result || std::wcscmp(token.termBuffer(), expected) != 0) {
            std::fwprintf(stderr, L"Expected [%ls], got [%ls]\n", expected,
                          result ? token.termBuffer() : L"end of stream");
            return 1;
        }
    }
    const bool finished = !tokens->next(&token);
    if (!finished) std::fwprintf(stderr, L"Unexpected final token [%ls]\n", token.termBuffer());
    tokens->close();
    return finished ? 0 : 1;
}
TEST
%{__cxx} %{build_cxxflags} -I%{buildroot}%{_includedir} -I%{buildroot}%{_includedir}/CLucene/ext check-cjk.cpp \
    %{build_ldflags} -L%{buildroot}%{_libdir} -Wl,-rpath-link,%{buildroot}%{_libdir} -lclucene-contribs-lib -lclucene-core -o check-cjk
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./check-cjk

%files
%doc README
%license APACHE.license LGPL.license COPYING
%{_libdir}/libclucene-*.so.*

%files devel
%{_includedir}/CLucene/
%{_includedir}/CLucene.h
%{_libdir}/libclucene-*.so
%{_libdir}/pkgconfig/libclucene-core.pc
%{_libdir}/CLuceneConfig.cmake/

%changelog
%autochangelog
