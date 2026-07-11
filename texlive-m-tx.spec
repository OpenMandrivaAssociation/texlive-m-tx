%global tl_name m-tx
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.63d
Release:	%{tl_revision}.1
Summary:	A preprocessor for pmx
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/m-tx
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/m-tx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/m-tx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(m-tx.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
M-Tx is a preprocessor to pmx, which is itself a preprocessor to
musixtex, a music typesetting system. The prime motivation to the
development of M-Tx was to provide lyrics for music to be typeset. In
fact, pmx now provides a lyrics interface, but M-Tx continues in use by
those who prefer its language.

