# TODO:
# - add pflogsumm.cron
%include	/usr/lib/rpm/macros.perl
Summary:	Postfix Log Entry Summarizer
Summary(pl):	Analizator logów postfiksa
Name:		pflogsumm
Version:	1.0.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://jimsun.linxnet.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	41e77528a99e22514c56e1a9bdf67bce
# Source1:	%{name}.cron
URL:		http://jimsun.linxnet.com/postfix_contrib.html
BuildRequires:	rpm-perlprov >= 4.0.2-106
Requires:	perl >= 5.6.1
Requires:	perl-modules >= 5.6.1
Requires:	perl-Date-Calc >= 5.3
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
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}
# install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,/etc/cron.daily}

install pflogsumm.pl $RPM_BUILD_ROOT%{_sbindir}
install pflogsumm.1 $RPM_BUILD_ROOT%{_mandir}/man1
# install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog pflogsumm-faq.txt README rem_smtpd_stats_supp.pl ToDo
%attr(755,root,root) %{_sbindir}/pflogsumm.pl
# %attr(755,root,root) /etc/cron.daily/%{name}
%{_mandir}/man1/*
