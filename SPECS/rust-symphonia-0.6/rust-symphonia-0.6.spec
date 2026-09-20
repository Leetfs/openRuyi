# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia
%global full_version 0.6.0
%global pkgname symphonia-0.6

Name:           rust-symphonia-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:1758d6c853020a7244de03cc3e0185eaea3f58715122422dd3cc7452e6d4c16a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0
Requires:       crate(symphonia-metadata-0.6) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "symphonia"

%package     -n %{name}+aac
Summary:        Pure Rust media container and audio decoding library - feature "aac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-codec-aac-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/aac) = %{version}

%description -n %{name}+aac
This metapackage enables feature "aac" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+adpcm
Summary:        Pure Rust media container and audio decoding library - feature "adpcm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-codec-adpcm-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/adpcm) = %{version}

%description -n %{name}+adpcm
This metapackage enables feature "adpcm" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aiff
Summary:        Pure Rust media container and audio decoding library - feature "aiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-format-riff-0.6) >= 0.6.0
Requires:       crate(symphonia-format-riff-0.6/aiff) >= 0.6.0
Provides:       crate(%{pkgname}/aiff) = %{version}

%description -n %{name}+aiff
This metapackage enables feature "aiff" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alac
Summary:        Pure Rust media container and audio decoding library - feature "alac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-codec-alac-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/alac) = %{version}

%description -n %{name}+alac
This metapackage enables feature "alac" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Pure Rust media container and audio decoding library - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-codecs) = %{version}
Requires:       crate(%{pkgname}/all-formats) = %{version}
Requires:       crate(%{pkgname}/all-meta) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-codecs
Summary:        Pure Rust media container and audio decoding library - feature "all-codecs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aac) = %{version}
Requires:       crate(%{pkgname}/adpcm) = %{version}
Requires:       crate(%{pkgname}/alac) = %{version}
Requires:       crate(%{pkgname}/flac) = %{version}
Requires:       crate(%{pkgname}/mp1) = %{version}
Requires:       crate(%{pkgname}/mp2) = %{version}
Requires:       crate(%{pkgname}/mp3) = %{version}
Requires:       crate(%{pkgname}/pcm) = %{version}
Requires:       crate(%{pkgname}/vorbis) = %{version}
Provides:       crate(%{pkgname}/all-codecs) = %{version}

%description -n %{name}+all-codecs
This metapackage enables feature "all-codecs" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-formats
Summary:        Pure Rust media container and audio decoding library - feature "all-formats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aiff) = %{version}
Requires:       crate(%{pkgname}/caf) = %{version}
Requires:       crate(%{pkgname}/isomp4) = %{version}
Requires:       crate(%{pkgname}/mkv) = %{version}
Requires:       crate(%{pkgname}/ogg) = %{version}
Requires:       crate(%{pkgname}/wav) = %{version}
Provides:       crate(%{pkgname}/all-formats) = %{version}

%description -n %{name}+all-formats
This metapackage enables feature "all-formats" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-meta
Summary:        Pure Rust media container and audio decoding library - feature "all-meta"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ape) = %{version}
Requires:       crate(%{pkgname}/id3v1) = %{version}
Requires:       crate(%{pkgname}/id3v2) = %{version}
Provides:       crate(%{pkgname}/all-meta) = %{version}

%description -n %{name}+all-meta
This metapackage enables feature "all-meta" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ape
Summary:        Pure Rust media container and audio decoding library - feature "ape"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-metadata-0.6/ape) >= 0.6.0
Provides:       crate(%{pkgname}/ape) = %{version}

%description -n %{name}+ape
This metapackage enables feature "ape" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+caf
Summary:        Pure Rust media container and audio decoding library - feature "caf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-format-caf-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/caf) = %{version}

%description -n %{name}+caf
This metapackage enables feature "caf" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust media container and audio decoding library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/adpcm) = %{version}
Requires:       crate(%{pkgname}/all-meta) = %{version}
Requires:       crate(%{pkgname}/flac) = %{version}
Requires:       crate(%{pkgname}/mkv) = %{version}
Requires:       crate(%{pkgname}/ogg) = %{version}
Requires:       crate(%{pkgname}/opt-simd) = %{version}
Requires:       crate(%{pkgname}/pcm) = %{version}
Requires:       crate(%{pkgname}/vorbis) = %{version}
Requires:       crate(%{pkgname}/wav) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+exp-subtitle-codecs
Summary:        Pure Rust media container and audio decoding library - feature "exp-subtitle-codecs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-core-0.6/exp-subtitle-codecs) >= 0.6.0
Provides:       crate(%{pkgname}/exp-subtitle-codecs) = %{version}

%description -n %{name}+exp-subtitle-codecs
This metapackage enables feature "exp-subtitle-codecs" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+exp-video-codecs
Summary:        Pure Rust media container and audio decoding library - feature "exp-video-codecs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-core-0.6/exp-video-codecs) >= 0.6.0
Provides:       crate(%{pkgname}/exp-video-codecs) = %{version}

%description -n %{name}+exp-video-codecs
This metapackage enables feature "exp-video-codecs" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flac
Summary:        Pure Rust media container and audio decoding library - feature "flac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-bundle-flac-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/flac) = %{version}

%description -n %{name}+flac
This metapackage enables feature "flac" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+id3v1
Summary:        Pure Rust media container and audio decoding library - feature "id3v1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-metadata-0.6/id3v1) >= 0.6.0
Provides:       crate(%{pkgname}/id3v1) = %{version}

%description -n %{name}+id3v1
This metapackage enables feature "id3v1" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+id3v2
Summary:        Pure Rust media container and audio decoding library - feature "id3v2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-metadata-0.6/id3v2) >= 0.6.0
Provides:       crate(%{pkgname}/id3v2) = %{version}

%description -n %{name}+id3v2
This metapackage enables feature "id3v2" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+isomp4
Summary:        Pure Rust media container and audio decoding library - feature "isomp4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-format-isomp4-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/isomp4) = %{version}

%description -n %{name}+isomp4
This metapackage enables feature "isomp4" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mkv
Summary:        Pure Rust media container and audio decoding library - feature "mkv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-format-mkv-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/mkv) = %{version}

%description -n %{name}+mkv
This metapackage enables feature "mkv" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mp1
Summary:        Pure Rust media container and audio decoding library - feature "mp1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-bundle-mp3-0.6) >= 0.6.0
Requires:       crate(symphonia-bundle-mp3-0.6/mp1) >= 0.6.0
Provides:       crate(%{pkgname}/mp1) = %{version}

%description -n %{name}+mp1
This metapackage enables feature "mp1" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mp2
Summary:        Pure Rust media container and audio decoding library - feature "mp2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-bundle-mp3-0.6) >= 0.6.0
Requires:       crate(symphonia-bundle-mp3-0.6/mp2) >= 0.6.0
Provides:       crate(%{pkgname}/mp2) = %{version}

%description -n %{name}+mp2
This metapackage enables feature "mp2" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mp3
Summary:        Pure Rust media container and audio decoding library - feature "mp3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-bundle-mp3-0.6) >= 0.6.0
Requires:       crate(symphonia-bundle-mp3-0.6/mp3) >= 0.6.0
Provides:       crate(%{pkgname}/mp3) = %{version}

%description -n %{name}+mp3
This metapackage enables feature "mp3" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mpa
Summary:        Pure Rust media container and audio decoding library - feature "mpa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mp1) = %{version}
Requires:       crate(%{pkgname}/mp2) = %{version}
Requires:       crate(%{pkgname}/mp3) = %{version}
Provides:       crate(%{pkgname}/mpa) = %{version}

%description -n %{name}+mpa
This metapackage enables feature "mpa" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ogg
Summary:        Pure Rust media container and audio decoding library - feature "ogg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-format-ogg-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/ogg) = %{version}

%description -n %{name}+ogg
This metapackage enables feature "ogg" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd
Summary:        Pure Rust media container and audio decoding library - feature "opt-simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/opt-simd-avx) = %{version}
Requires:       crate(%{pkgname}/opt-simd-neon) = %{version}
Requires:       crate(%{pkgname}/opt-simd-sse) = %{version}
Provides:       crate(%{pkgname}/opt-simd) = %{version}

%description -n %{name}+opt-simd
This metapackage enables feature "opt-simd" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd-avx
Summary:        Pure Rust media container and audio decoding library - feature "opt-simd-avx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-core-0.6/opt-simd-avx) >= 0.6.0
Provides:       crate(%{pkgname}/opt-simd-avx) = %{version}

%description -n %{name}+opt-simd-avx
This metapackage enables feature "opt-simd-avx" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd-neon
Summary:        Pure Rust media container and audio decoding library - feature "opt-simd-neon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-core-0.6/opt-simd-neon) >= 0.6.0
Provides:       crate(%{pkgname}/opt-simd-neon) = %{version}

%description -n %{name}+opt-simd-neon
This metapackage enables feature "opt-simd-neon" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd-sse
Summary:        Pure Rust media container and audio decoding library - feature "opt-simd-sse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-core-0.6/opt-simd-sse) >= 0.6.0
Provides:       crate(%{pkgname}/opt-simd-sse) = %{version}

%description -n %{name}+opt-simd-sse
This metapackage enables feature "opt-simd-sse" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pcm
Summary:        Pure Rust media container and audio decoding library - feature "pcm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-codec-pcm-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/pcm) = %{version}

%description -n %{name}+pcm
This metapackage enables feature "pcm" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vorbis
Summary:        Pure Rust media container and audio decoding library - feature "vorbis"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-codec-vorbis-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/vorbis) = %{version}

%description -n %{name}+vorbis
This metapackage enables feature "vorbis" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wav
Summary:        Pure Rust media container and audio decoding library - feature "wav"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-format-riff-0.6) >= 0.6.0
Requires:       crate(symphonia-format-riff-0.6/wav) >= 0.6.0
Provides:       crate(%{pkgname}/wav) = %{version}

%description -n %{name}+wav
This metapackage enables feature "wav" for the Rust symphonia crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
