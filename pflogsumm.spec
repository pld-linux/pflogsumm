%include	/usr/lib/rpm/macros.perl
Summary:	Postfix Log Entry Summarizer
Summary(pl):	Analizator logów postfiksa
Name:		pflogsumm
Version:	1.0.12
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://jimsun.linxnet.com/pub/postfix_contrib/%{name}-%{version}.tar.gz
# Source0-md5:	45e2d25a21c5a082769d8903e04d3ea8
Source1:	%{name}.sysconfig
Source2:	%{name}.cron
URL:		http://jimsun.linxnet.com/postfix_contrib.html
BuildRequires:	rpm-perlprov >= 4.0.2-106
Requires:	crondaemon
Requires:	smtpdaemon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The programme serves a detailed log analysis of mail server.

%description -l pl
Program slu¿±cy do szczegó³owej analizy logów serwera pocztowego.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,/etc/{cron.daily,sysconfig}}

install pflogsumm.pl $RPM_BUILD_ROOT%{_sbindir}
install pflogsumm.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.daily/00-%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog pflogsumm-faq.txt README rem_smtpd_stats_supp.pl ToDo
%attr(755,root,root) %{_sbindir}/pflogsumm.pl
%attr(750,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/cron.daily/00-%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/%{name}
%{_mandir}/man1/*
