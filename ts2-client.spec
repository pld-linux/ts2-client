Summary:	TeamSpeak2 client
Summary(pl):	Klient TeamSpeak2
Name:		ts2-client
Version:	rc2_2032
Release:	1
License:	freeware
Group:		Applications/Communications
Source0:	ftp://webpost.teamspeak.org/releases/ts2_client_%{version}.tar.bz2
# Source0-md5:	e93d17a25e07b1cbe400e4eb028ca8f8
URL:		http://www.teamspeak.org/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoprovfiles        %{_libdir}/ts2/.*\.so.*

%description
TeamSpeak was primarily designed to work for people who are behind a
NAT router (share internet). Further more it was designed for gamers.
That mean to us it had to use as little bandwidth as possible, while
having a reasonable voice quality. The authors think they achieved
that with the 650 bytes/s maximum CELP codec.

%description -l pl
TeamSpeak zosta³ zaprojektowany g³ównie do pracy dla ludzi za
routerami z maskowaniem adresów (dziel±cymi Internet). Ponadto by³
pomy¶lany dla graczy. Oznacza to, ¿e ma zu¿ywaæ jak najmniej pasma,
zapewniaj±c rozs±dn± jako¶æ g³osu. Autorzy uwa¿aj±, ¿e osi±gnêli to
przy pomocy kodeka CELP z maksimum 650 bajtów/sekundê.

%prep
%setup -q -n ts2_client_%{version}/setup.data/image

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ts2}

install TeamSpeak.bin $RPM_BUILD_ROOT%{_bindir}/TeamSpeak.bin
sed -e 's#=%installdir%#=%{_prefix}/lib/ts2#;s#%installdir%#%{_bindir}#' TeamSpeak > $RPM_BUILD_ROOT%{_bindir}/TeamSpeak
install lib* $RPM_BUILD_ROOT%{_libdir}/ts2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc manual/* Readme.txt clicense.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ts2
