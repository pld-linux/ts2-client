Summary:	TeamSpeak2 client
Summary(pl):	Klient TeamSpeak2
Name:		ts2-client
Version:	rc2_2032
Release:	2
License:	Freeware
Group:		Applications/Communications
Source0:	ftp://ftp.freenet.de/pub/4players/teamspeak.org/releases/ts2_client_%{version}.tar.bz2
# Source0-md5:	e93d17a25e07b1cbe400e4eb028ca8f8
Source1:	%{name}.sh
Source2:	%{name}.desktop
URL:		http://www.goteamspeak.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/ts2/.*\.so.*

%description
TeamSpeak was primarily designed to work for people who are behind a
NAT router (share internet). Further more it was designed for gamers.
That mean to us it had to use as little bandwidth as possible, while
having a reasonable voice quality. The authors think they achieved
that with the 650 bytes/s maximum CELP codec.

%description -l pl
TeamSpeak zosta� zaprojektowany g��wnie do pracy dla ludzi za
routerami z maskowaniem adres�w (dziel�cymi Internet). Ponadto by�
pomy�lany dla graczy. Oznacza to, �e ma zu�ywa� jak najmniej pasma,
zapewniaj�c rozs�dn� jako�� g�osu. Autorzy uwa�aj�, �e osi�gn�li to
przy pomocy kodeka CELP z maksimum 650 bajt�w/sekund�.

%prep
%setup -q -n ts2_client_%{version}/setup.data/image

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ts2} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_datadir}/ts2/sounds}\

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/TeamSpeak
install TeamSpeak.bin $RPM_BUILD_ROOT%{_libdir}/ts2/TeamSpeak
install lib* $RPM_BUILD_ROOT%{_libdir}/ts2

install sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/ts2/sounds
ln -s ../../share/ts2/sounds $RPM_BUILD_ROOT%{_libdir}/ts2

install icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/ts2.xpm
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/ts2.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc manual/* Readme.txt clicense.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ts2
%attr(644,root,root) %{_desktopdir}/*
%attr(644,root,root) %{_pixmapsdir}/*
%{_datadir}/ts2
