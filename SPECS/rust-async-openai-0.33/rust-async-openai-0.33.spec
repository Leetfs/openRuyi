# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-openai
%global full_version 0.33.1
%global pkgname async-openai-0.33

Name:           rust-async-openai-0.33
Version:        0.33.1
Release:        %autorelease
Summary:        Rust crate "async-openai"
License:        MIT
URL:            https://github.com/64bit/async-openai
#!RemoteAsset:  sha256:cc48c3deb4ad9a2ee8c8e364c79eb0f74e69e17ed7e883d55988b90ea44fe986
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.3/default) >= 0.3.4
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.4
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-1/rc) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.150

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "async-openai"

%package     -n %{name}+api
Summary:        OpenAI - feature "_api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-openai-macros-0.1/default) >= 0.1.1
Requires:       crate(backoff-0.4/default) >= 0.4.0
Requires:       crate(backoff-0.4/tokio) >= 0.4.0
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(eventsource-stream-0.2/default) >= 0.2.3
Requires:       crate(futures-0.3/default) >= 0.3.32
Requires:       crate(rand-0.9/default) >= 0.9.5
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/multipart) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(reqwest-eventsource-0.6/default) >= 0.6.0
Requires:       crate(secrecy-0.10/default) >= 0.10.3
Requires:       crate(secrecy-0.10/serde) >= 0.10.3
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.53.1
Requires:       crate(tokio-1/fs) >= 1.53.1
Requires:       crate(tokio-1/macros) >= 1.53.1
Requires:       crate(tokio-stream-0.1/default) >= 0.1.18
Requires:       crate(tokio-util-0.7/codec) >= 0.7.18
Requires:       crate(tokio-util-0.7/default) >= 0.7.18
Requires:       crate(tokio-util-0.7/io-util) >= 0.7.18
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(url-2/default) >= 2.5.8
Provides:       crate(%{pkgname}/api) = %{version}

%description -n %{name}+api
This metapackage enables feature "_api" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+administration
Summary:        OpenAI - feature "administration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/administration-types) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Provides:       crate(%{pkgname}/administration) = %{version}

%description -n %{name}+administration
This metapackage enables feature "administration" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+administration-types
Summary:        OpenAI - feature "administration-types" and 9 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/administration-types) = %{version}
Provides:       crate(%{pkgname}/assistant-types) = %{version}
Provides:       crate(%{pkgname}/batch-types) = %{version}
Provides:       crate(%{pkgname}/chatkit-types) = %{version}
Provides:       crate(%{pkgname}/embedding-types) = %{version}
Provides:       crate(%{pkgname}/model-types) = %{version}
Provides:       crate(%{pkgname}/moderation-types) = %{version}
Provides:       crate(%{pkgname}/response-types) = %{version}
Provides:       crate(%{pkgname}/vectorstore-types) = %{version}
Provides:       crate(%{pkgname}/webhook-types) = %{version}

%description -n %{name}+administration-types
This metapackage enables feature "administration-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "assistant-types", "batch-types", "chatkit-types", "embedding-types", "model-types", "moderation-types", "response-types", "vectorstore-types", and "webhook-types" features.

%package     -n %{name}+assistant
Summary:        OpenAI - feature "assistant"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/assistant-types) = %{version}
Provides:       crate(%{pkgname}/assistant) = %{version}

%description -n %{name}+assistant
This metapackage enables feature "assistant" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+audio
Summary:        OpenAI - feature "audio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/audio-types) = %{version}
Provides:       crate(%{pkgname}/audio) = %{version}

%description -n %{name}+audio
This metapackage enables feature "audio" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+audio-types
Summary:        OpenAI - feature "audio-types" and 6 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/audio-types) = %{version}
Provides:       crate(%{pkgname}/chat-completion-types) = %{version}
Provides:       crate(%{pkgname}/container-types) = %{version}
Provides:       crate(%{pkgname}/file-types) = %{version}
Provides:       crate(%{pkgname}/image-types) = %{version}
Provides:       crate(%{pkgname}/skill-types) = %{version}
Provides:       crate(%{pkgname}/video-types) = %{version}

%description -n %{name}+audio-types
This metapackage enables feature "audio-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "chat-completion-types", "container-types", "file-types", "image-types", "skill-types", and "video-types" features.

%package     -n %{name}+batch
Summary:        OpenAI - feature "batch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/batch-types) = %{version}
Provides:       crate(%{pkgname}/batch) = %{version}

%description -n %{name}+batch
This metapackage enables feature "batch" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+byot
Summary:        OpenAI - feature "byot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-openai-macros-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/byot) = %{version}

%description -n %{name}+byot
This metapackage enables feature "byot" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chat-completion
Summary:        OpenAI - feature "chat-completion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/chat-completion-types) = %{version}
Provides:       crate(%{pkgname}/chat-completion) = %{version}

%description -n %{name}+chat-completion
This metapackage enables feature "chat-completion" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chatkit
Summary:        OpenAI - feature "chatkit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/chatkit-types) = %{version}
Provides:       crate(%{pkgname}/chatkit) = %{version}

%description -n %{name}+chatkit
This metapackage enables feature "chatkit" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+completion-types
Summary:        OpenAI - feature "completion-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chat-completion-types) = %{version}
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/completion-types) = %{version}

%description -n %{name}+completion-types
This metapackage enables feature "completion-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+completions
Summary:        OpenAI - feature "completions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/completion-types) = %{version}
Provides:       crate(%{pkgname}/completions) = %{version}

%description -n %{name}+completions
This metapackage enables feature "completions" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+container
Summary:        OpenAI - feature "container"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/container-types) = %{version}
Provides:       crate(%{pkgname}/container) = %{version}

%description -n %{name}+container
This metapackage enables feature "container" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+embedding
Summary:        OpenAI - feature "embedding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/embedding-types) = %{version}
Provides:       crate(%{pkgname}/embedding) = %{version}

%description -n %{name}+embedding
This metapackage enables feature "embedding" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+eval-types
Summary:        OpenAI - feature "eval-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chat-completion-types) = %{version}
Requires:       crate(%{pkgname}/grader-types) = %{version}
Requires:       crate(%{pkgname}/response-types) = %{version}
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/eval-types) = %{version}

%description -n %{name}+eval-types
This metapackage enables feature "eval-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+evals
Summary:        OpenAI - feature "evals"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/eval-types) = %{version}
Provides:       crate(%{pkgname}/evals) = %{version}

%description -n %{name}+evals
This metapackage enables feature "evals" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+file
Summary:        OpenAI - feature "file"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/file-types) = %{version}
Provides:       crate(%{pkgname}/file) = %{version}

%description -n %{name}+file
This metapackage enables feature "file" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+finetuning
Summary:        OpenAI - feature "finetuning"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/finetuning-types) = %{version}
Provides:       crate(%{pkgname}/finetuning) = %{version}

%description -n %{name}+finetuning
This metapackage enables feature "finetuning" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+finetuning-types
Summary:        OpenAI - feature "finetuning-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/grader-types) = %{version}
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/finetuning-types) = %{version}

%description -n %{name}+finetuning-types
This metapackage enables feature "finetuning-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        OpenAI - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/administration) = %{version}
Requires:       crate(%{pkgname}/assistant) = %{version}
Requires:       crate(%{pkgname}/audio) = %{version}
Requires:       crate(%{pkgname}/batch) = %{version}
Requires:       crate(%{pkgname}/byot) = %{version}
Requires:       crate(%{pkgname}/chat-completion) = %{version}
Requires:       crate(%{pkgname}/chatkit) = %{version}
Requires:       crate(%{pkgname}/completions) = %{version}
Requires:       crate(%{pkgname}/container) = %{version}
Requires:       crate(%{pkgname}/embedding) = %{version}
Requires:       crate(%{pkgname}/evals) = %{version}
Requires:       crate(%{pkgname}/file) = %{version}
Requires:       crate(%{pkgname}/finetuning) = %{version}
Requires:       crate(%{pkgname}/image) = %{version}
Requires:       crate(%{pkgname}/model) = %{version}
Requires:       crate(%{pkgname}/moderation) = %{version}
Requires:       crate(%{pkgname}/realtime) = %{version}
Requires:       crate(%{pkgname}/responses) = %{version}
Requires:       crate(%{pkgname}/skill) = %{version}
Requires:       crate(%{pkgname}/types) = %{version}
Requires:       crate(%{pkgname}/upload) = %{version}
Requires:       crate(%{pkgname}/vectorstore) = %{version}
Requires:       crate(%{pkgname}/video) = %{version}
Requires:       crate(%{pkgname}/webhook) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+grader-types
Summary:        OpenAI - feature "grader-types" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eval-types) = %{version}
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/grader) = %{version}
Provides:       crate(%{pkgname}/grader-types) = %{version}

%description -n %{name}+grader-types
This metapackage enables feature "grader-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "grader" feature.

%package     -n %{name}+image
Summary:        OpenAI - feature "image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/image-types) = %{version}
Provides:       crate(%{pkgname}/image) = %{version}

%description -n %{name}+image
This metapackage enables feature "image" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+model
Summary:        OpenAI - feature "model"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/model-types) = %{version}
Provides:       crate(%{pkgname}/model) = %{version}

%description -n %{name}+model
This metapackage enables feature "model" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+moderation
Summary:        OpenAI - feature "moderation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/moderation-types) = %{version}
Provides:       crate(%{pkgname}/moderation) = %{version}

%description -n %{name}+moderation
This metapackage enables feature "moderation" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        OpenAI - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/multipart) >= 0.12.28
Requires:       crate(reqwest-0.12/native-tls) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        OpenAI - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/multipart) >= 0.12.28
Requires:       crate(reqwest-0.12/native-tls-vendored) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+realtime
Summary:        OpenAI - feature "realtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/realtime-types) = %{version}
Requires:       crate(tokio-tungstenite-0.28) >= 0.28.0
Provides:       crate(%{pkgname}/realtime) = %{version}

%description -n %{name}+realtime
This metapackage enables feature "realtime" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+realtime-types
Summary:        OpenAI - feature "realtime-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/response-types) = %{version}
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/realtime-types) = %{version}

%description -n %{name}+realtime-types
This metapackage enables feature "realtime-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+responses
Summary:        OpenAI - feature "responses"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/response-types) = %{version}
Provides:       crate(%{pkgname}/responses) = %{version}

%description -n %{name}+responses
This metapackage enables feature "responses" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        OpenAI - feature "rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/multipart) >= 0.12.28
Requires:       crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+rustls-webpki-roots
Summary:        OpenAI - feature "rustls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/multipart) >= 0.12.28
Requires:       crate(reqwest-0.12/rustls-tls-webpki-roots) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Provides:       crate(%{pkgname}/rustls-webpki-roots) = %{version}

%description -n %{name}+rustls-webpki-roots
This metapackage enables feature "rustls-webpki-roots" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+skill
Summary:        OpenAI - feature "skill"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/skill-types) = %{version}
Provides:       crate(%{pkgname}/skill) = %{version}

%description -n %{name}+skill
This metapackage enables feature "skill" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+types
Summary:        OpenAI - feature "types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/administration-types) = %{version}
Requires:       crate(%{pkgname}/assistant-types) = %{version}
Requires:       crate(%{pkgname}/audio-types) = %{version}
Requires:       crate(%{pkgname}/batch-types) = %{version}
Requires:       crate(%{pkgname}/chat-completion-types) = %{version}
Requires:       crate(%{pkgname}/chatkit-types) = %{version}
Requires:       crate(%{pkgname}/completion-types) = %{version}
Requires:       crate(%{pkgname}/container-types) = %{version}
Requires:       crate(%{pkgname}/embedding-types) = %{version}
Requires:       crate(%{pkgname}/eval-types) = %{version}
Requires:       crate(%{pkgname}/file-types) = %{version}
Requires:       crate(%{pkgname}/finetuning-types) = %{version}
Requires:       crate(%{pkgname}/grader-types) = %{version}
Requires:       crate(%{pkgname}/image-types) = %{version}
Requires:       crate(%{pkgname}/model-types) = %{version}
Requires:       crate(%{pkgname}/moderation-types) = %{version}
Requires:       crate(%{pkgname}/realtime-types) = %{version}
Requires:       crate(%{pkgname}/response-types) = %{version}
Requires:       crate(%{pkgname}/skill-types) = %{version}
Requires:       crate(%{pkgname}/upload-types) = %{version}
Requires:       crate(%{pkgname}/vectorstore-types) = %{version}
Requires:       crate(%{pkgname}/video-types) = %{version}
Requires:       crate(%{pkgname}/webhook-types) = %{version}
Provides:       crate(%{pkgname}/types) = %{version}

%description -n %{name}+types
This metapackage enables feature "types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+upload
Summary:        OpenAI - feature "upload"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/upload-types) = %{version}
Provides:       crate(%{pkgname}/upload) = %{version}

%description -n %{name}+upload
This metapackage enables feature "upload" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+upload-types
Summary:        OpenAI - feature "upload-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/file-types) = %{version}
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}/upload-types) = %{version}

%description -n %{name}+upload-types
This metapackage enables feature "upload-types" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vectorstore
Summary:        OpenAI - feature "vectorstore"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/vectorstore-types) = %{version}
Provides:       crate(%{pkgname}/vectorstore) = %{version}

%description -n %{name}+vectorstore
This metapackage enables feature "vectorstore" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+video
Summary:        OpenAI - feature "video"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api) = %{version}
Requires:       crate(%{pkgname}/video-types) = %{version}
Provides:       crate(%{pkgname}/video) = %{version}

%description -n %{name}+video
This metapackage enables feature "video" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webhook
Summary:        OpenAI - feature "webhook"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/webhook-types) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(hex-0.4) >= 0.4.3
Requires:       crate(hmac-0.12) >= 0.12.1
Requires:       crate(sha2-0.10) >= 0.10.9
Requires:       crate(thiserror-2/default) >= 2.0.18
Provides:       crate(%{pkgname}/webhook) = %{version}

%description -n %{name}+webhook
This metapackage enables feature "webhook" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
