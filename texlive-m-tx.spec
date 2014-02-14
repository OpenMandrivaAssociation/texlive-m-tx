# revision 32525
# category Package
# catalog-ctan /support/m-tx
# catalog-date 2013-12-25 07:39:11 +0100
# catalog-license gpl
# catalog-version 0.60d
Name:		texlive-m-tx
Version:	0.60d
Release:	7
Summary:	A preprocessor for pmx
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/m-tx
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/m-tx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/m-tx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-m-tx.bin

%description
M-Tx is a preprocessor to pmx, which is itself a preprocessor
to musixtex, a music typesetting system. The prime motivation
to the development of M-Tx was to provide lyrics for music to
be typeset. In fact, pmx now provides a lyrics interface, but
M-Tx continues in use by those who prefer its language.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/m-tx
%{_texmfdistdir}/scripts/m-tx/m-tx.lua
%{_texmfdistdir}/tex/generic/m-tx/mtx.tex
%doc %{_texmfdistdir}/doc/generic/m-tx/README
%doc %{_texmfdistdir}/doc/generic/m-tx/m-tx.html
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx-install.pdf
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx-install.tex
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060.pdf
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/Makefile
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/README.M-Txdoc
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/borup.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/chord.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/dertod.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/docversion
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/dona.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/dwoman.mta
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/dwoman.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/halleluja.ltx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/kanons.ltx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/kroonhom.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/loofnou.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/lyrics.tex
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/macro.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/make-dvi
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/make-pdf
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/make-target
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma.mta
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma1.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma2.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma3.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma4.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma5.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/melisma6.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/meter.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/mozart.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/mozart0.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/mtxdoc.sty
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/mtxdoc.tex
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/mtxindex.tex
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/mtxlatex.sty
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/netfirst.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/netsoos.mta
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/netsoos1.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/netsoos2.mtb
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/notes.tex
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/pdfcat
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/psalm42.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/sanctus.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/title.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/title1.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/viva.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/mtx060/volta.mtx
%doc %{_texmfdistdir}/doc/generic/m-tx/prepmx.html
%doc %{_mandir}/man1/m-tx.1*
%doc %{_texmfdistdir}/doc/man/man1/m-tx.man1.pdf
%doc %{_mandir}/man1/prepmx.1*
%doc %{_texmfdistdir}/doc/man/man1/prepmx.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/m-tx/m-tx.lua m-tx
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
