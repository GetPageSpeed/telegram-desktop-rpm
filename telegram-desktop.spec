%global upstream_github telegramdesktop
%global upstream_name tdesktop
%global lastversion_tag v%{version}
%global lastversion_dir %{upstream_name}-%{version}


%global debug_package %{nil}

Summary:	Telegram is a new era of messaging
Name:		telegram-desktop
Version:    4.6.1
Release: 1%{?dist}

Group:		Applications/Internet
License:	GPLv3
URL:		https://github.com/%{upstream_github}/%{upstream_name}
Source1:	%{url}/releases/download/%{lastversion_tag}/tsetup.%{version}.tar.xz

Source2:	telegram.png
Source3:	telegram.desktop
Source4:	%{name}.appdata.xml

BuildRequires:	desktop-file-utils
%if (0%{?suse_version})
BuildRequires:	appstream-glib
%else
BuildRequires:	libappstream-glib
%endif


%description
Telegram is a messaging app with a focus on speed and security, it’s super
fast, simple and free. You can use Telegram on all your devices at the same
time — your messages sync seamlessly across any of your phones, tablets or
computers.

With Telegram, you can send messages, photos, videos and files of any type
(doc, zip, mp3, etc), as well as create groups for up to 200 people. You can
write to your phone contacts and find people by their usernames. As a result,
Telegram is like SMS and email combined — and can take care of all your
personal or business messaging needs.


%prep
%setup -T -b 1 -q -n Telegram


%build
# nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

# cp -arf ./Telegram %{buildroot}%{_datadir}/%{name}/telegram
# cp -arf ./Updater %{buildroot}%{_datadir}/%{name}/updater
install -Dpm0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/pixmaps/telegram.png

# ln -s %{_datadir}/%{name}/telegram %{buildroot}%{_bindir}/telegram

install -D -m0755 ./Telegram %{buildroot}%{_bindir}/telegram

install -D -m0644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}.desktop

desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/%{name}.desktop

install -D -m0644 %{SOURCE4} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%files
%{_bindir}/telegram
%dir %{_datadir}/%{name}
#%%{_datadir}/%%{name}/telegram
#%%{_datadir}/%%{name}/updater
%{_datadir}/applications/telegram-desktop.desktop
%{_datadir}/pixmaps/telegram.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Tue Feb 07 2023 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.6.1


* Sat Feb 04 2023 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.6.0


* Sun Jan 08 2023 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.5.3


* Wed Jan 04 2023 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.5.2


* Tue Jan 03 2023 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.5.1


* Sat Dec 31 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.5.0


* Thu Dec 08 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.4.1


* Wed Dec 07 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.4.0


* Sat Nov 26 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.3.4


* Tue Nov 08 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.3.1


* Sun Nov 06 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.3.0


* Sat Oct 01 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.2.4


* Fri Sep 30 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.2.3


* Sat Sep 17 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.2.0


* Wed Aug 17 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.1.1


* Sat Aug 13 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.1.0


* Sun Jun 26 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.0.2


* Sat Jun 25 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v4.0.1


* Wed Jun 22 2022 Danila Vershinin <info@getpagespeed.com> 4.0.0-1
- release 4.0.0

* Wed Apr 27 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.7.3


* Tue Apr 26 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.7.2


* Thu Apr 21 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.7.1


* Mon Apr 18 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.7.0


* Thu Mar 17 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.6.1


* Sat Mar 12 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.6.0


* Wed Feb 09 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.5.2


* Sat Feb 05 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.5.1


* Tue Feb 01 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.5.0


* Thu Jan 20 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.4.8


* Tue Jan 04 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.4.3


* Sat Jan 01 2022 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.4.2


* Fri Dec 31 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.4.0


* Thu Dec 09 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.3.0


* Wed Nov 17 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.2.5


* Sun Nov 14 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.2.4


* Wed Nov 10 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.2.3


* Sat Nov 06 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.2.2


* Thu Nov 04 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.2.1


* Sat Oct 30 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.1.11


* Sat Oct 09 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.1.9


* Sun Sep 26 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.1.1


* Mon Sep 20 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.1.0


* Thu Sep 02 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v3.0.1


* Wed Sep 01 2021 Danila Vershinin <info@getpagespeed.com> 3.0.0-1
- release 3.0.0

* Thu Aug 12 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v2.9.3


* Sat Jul 31 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v2.9.0


* Mon Jul 19 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v2.8.11


* Fri Jul 16 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v2.8.10


* Fri Jul 16 2021 Danila Vershinin <info@getpagespeed.com>
- upstream release v2.8.10

* Fri Jul 16 2021 Danila Vershinin <info@getpagespeed.com> 2.8.8-1
- release 2.8.8

* Fri Jul 02 2021 Danila Vershinin <info@getpagespeed.com> 2.8.4-1
- release 2.8.4

* Tue Jun 29 2021 Danila Vershinin <info@getpagespeed.com> 2.8.3-1
- release 2.8.3

* Sun Jun 27 2021 Danila Vershinin <info@getpagespeed.com> 2.8.1-1
- release 2.8.1

* Thu Apr 29 2021 Danila Vershinin <info@getpagespeed.com> 2.7.4-1
- release 2.7.4

* Wed Apr 28 2021 Danila Vershinin <info@getpagespeed.com> 2.7.3-1
- release 2.7.3

* Tue Apr 27 2021 Danila Vershinin <info@getpagespeed.com> 2.7.2-1
- release 2.7.2

* Sun Mar 21 2021 Danila Vershinin <info@getpagespeed.com> 2.7.1-1
- release 2.7.1

* Sat Mar 20 2021 Danila Vershinin <info@getpagespeed.com> 2.7.0-1
- release 2.7.0

* Thu Feb 25 2021 Danila Vershinin <info@getpagespeed.com> 2.6.1-1
- release 2.6.1

* Wed Feb 24 2021 Danila Vershinin <info@getpagespeed.com> 2.6.0-1
- release 2.6.0

* Thu Feb 18 2021 Danila Vershinin <info@getpagespeed.com> 2.5.9-1
- release 2.5.9

* Sat Jan 30 2021 Danila Vershinin <info@getpagespeed.com> 2.5.8-1
- release 2.5.8

* Fri Jan 29 2021 Danila Vershinin <info@getpagespeed.com> 2.5.7-1
- release 2.5.7

* Thu Dec 24 2020 Danila Vershinin <info@getpagespeed.com> 2.5.1-1
- release 2.5.1

* Fri Nov 06 2020 Danila Vershinin <info@getpagespeed.com> 2.4.7-1
- release 2.4.7

* Tue Nov 03 2020 Danila Vershinin <info@getpagespeed.com> 2.4.6-1
- release 2.4.6

* Sat Oct 31 2020 Danila Vershinin <info@getpagespeed.com> 2.4.5-1
- release 2.4.5

* Sat Oct 24 2020 Danila Vershinin <info@getpagespeed.com> 2.4.4-1
- release 2.4.4

* Thu Oct 08 2020 Danila Vershinin <info@getpagespeed.com> 2.4.3-1
- release 2.4.3

* Sat Oct 03 2020 Danila Vershinin <info@getpagespeed.com> 2.4.2-1
- release 2.4.2

* Thu Oct 01 2020 Danila Vershinin <info@getpagespeed.com> 2.4.0-1
- release 2.4.0

* Mon Aug 24 2020 Danila Vershinin <info@getpagespeed.com> 2.3.2-1
- release 2.3.2

* Sun Aug 23 2020 Danila Vershinin <info@getpagespeed.com> 2.3.1-1
- release 2.3.1

* Sat Aug 15 2020 Danila Vershinin <info@getpagespeed.com> 2.3.0-1
- release 2.3.0

* Mon Jul 27 2020 Danila Vershinin <info@getpagespeed.com> 2.2.0-1
- release 2.2.0

* Thu Jun 25 2020 Danila Vershinin <info@getpagespeed.com> 2.1.13-1
- release 2.1.13

* Fri Jun 19 2020 Danila Vershinin <info@getpagespeed.com> 2.1.12-1
- release 2.1.12

* Tue Jun 09 2020 Danila Vershinin <info@getpagespeed.com> 2.1.11-1
- release 2.1.11

* Sat Jun 06 2020 Danila Vershinin <info@getpagespeed.com> 2.1.10-1
- release 2.1.10

* Mon May 25 2020 Danila Vershinin <info@getpagespeed.com> 2.1.7-1
- release 2.1.7

* Fri May 15 2020 Danila Vershinin <info@getpagespeed.com> 2.1.6-1
- release 2.1.6

* Thu May 14 2020 Danila Vershinin <info@getpagespeed.com> 2.1.5-1
- release 2.1.5

* Sun May 10 2020 Danila Vershinin <info@getpagespeed.com> 2.1.4-1
- release 2.1.4

* Sat May 09 2020 Danila Vershinin <info@getpagespeed.com> 2.1.3-1
- release 2.1.3

* Wed May 06 2020 Danila Vershinin <info@getpagespeed.com> 2.1.2-1
- release 2.1.2

* Sat May 02 2020 Danila Vershinin <info@getpagespeed.com> 2.1.1-1
- release 2.1.1

* Fri Apr 24 2020 Danila Vershinin <info@getpagespeed.com> 2.1.0-1
- release 2.1.0

* Wed Apr 01 2020 Danila Vershinin <info@getpagespeed.com> 2.0.1-1
- upstream version auto-updated to 2.0.1

* Tue Mar 31 2020 Danila Vershinin <info@getpagespeed.com> 2.0.0-1
- upstream version auto-updated to 2.0.0

* Wed Mar 18 2020 Danila Vershinin <info@getpagespeed.com> 1.9.21-1
- upstream version auto-updated to 1.9.21

* Wed Feb 19 2020 Danila Vershinin <info@getpagespeed.com> 1.9.14-1
- upstream version auto-updated to 1.9.14

* Tue Jan 28 2020 Danila Vershinin <info@getpagespeed.com> 1.9.9-1
- upstream version auto-updated to 1.9.9

* Wed Jan 22 2020 Danila Vershinin <info@getpagespeed.com> 1.9.6-1
- upstream version auto-updated to 1.9.6

* Sun Jan 19 2020 Danila Vershinin <info@getpagespeed.com> 1.9.4-1
- upstream version auto-updated to 1.9.4

* Wed Jan 01 2020 Danila Vershinin <info@getpagespeed.com> 1.9.3-1
- upstream version auto-updated to 1.9.3

* Thu Oct 10 2019 Danila Vershinin <info@getpagespeed.com> 1.8.15-1
- upstream version auto-updated to 1.8.15

* Tue Oct 08 2019 Danila Vershinin <info@getpagespeed.com> 1.8.15-1
- upstream version auto-updated to 1.8.15

* Fri Sep 06 2019 Danila Vershinin <info@getpagespeed.com> 1.8.3-1
- upstream version auto-updated to 1.8.3

* Wed Aug 21 2019 Danila Vershinin <info@getpagespeed.com> 1.8.2-1
- upstream version auto-updated to 1.8.2

* Sat Aug 10 2019 Danila Vershinin <info@getpagespeed.com> 1.8.1-1
- upstream version auto-updated to 1.8.1

* Thu Aug 01 2019 Danila Vershinin <info@getpagespeed.com> 1.7.15-1
- upstream version auto-updated to 1.7.15

* Sat Jul 20 2019 Danila Vershinin <info@getpagespeed.com> 1.7.14-1
- upstream version auto-updated to 1.7.14

* Sat Jul 20 2019 Danila Vershinin <info@getpagespeed.com> 1.7.15-1
- upstream version auto-updated to 1.7.15

* Mon Jul 08 2019 Danila Vershinin <info@getpagespeed.com> 1.7.14-1
- upstream version auto-updated to 1.7.14

* Sun Jul 07 2019 Danila Vershinin <info@getpagespeed.com> 1.7.13-1
- upstream version auto-updated to 1.7.13

* Sat Jul 06 2019 Danila Vershinin <info@getpagespeed.com> 1.7.11-1
- upstream version auto-updated to 1.7.11

* Thu Jun 27 2019 Danila Vershinin <info@getpagespeed.com> 1.7.10-2
- correct build architecture

* Tue Jun 25 2019 Danila Vershinin <info@getpagespeed.com> 1.7.10-1
- upstream version auto-updated to 1.7.10

* Sat Apr 13 2019 Danila Vershinin <info@getpagespeed.com> 1.6.7-1
- update to 1.6.7

* Wed Sep 14 2016 rkady L. Shane <ashejn@russianfedora.pro> 0.10.6-1
- update to 0.10.6

* Mon Aug  8 2016 rkady L. Shane <ashejn@russianfedora.pro> 0.10.1-2
- added appdata file

* Mon Aug  8 2016 rkady L. Shane <ashejn@russianfedora.pro> 0.10.1-1
- update to 0.10.1

* Thu Aug  4 2016 rkady L. Shane <ashejn@russianfedora.pro> 0.10.0-1
- update to 0.10.0

* Mon Jun 27 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.56-1.R
- update to 0.9.56

* Thu Jun 16 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.51-1.R
- update to 0.9.51

* Wed May 25 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.49-1.R
- update to 0.9.49

* Wed May 11 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.48-1.R
- update to 0.9.48

* Thu Apr 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.42-1.R
- update to 0.9.42

* Wed Apr 13 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.41-1.R
- update to 0.9.41

* Tue Apr  5 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.40-1.R
- update to 0.9.40

* Wed Mar 16 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.33-1.R
- update to 0.9.33

* Tue Mar 15 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.32-1.R
- update to 0.9.32

* Mon Feb 29 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.28-1.R
- update to 0.9.28

* Tue Feb 23 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.26-1.R
- update to 0.9.26

* Wed Feb 17 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.24-1.R
- update to 0.9.18

* Sun Jan 10 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.18-1.R
- update to 0.9.18

* Thu Dec 10 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.15-1.R
- update to 0.9.15

* Thu Nov 26 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.13-1.R
- update to 0.9.13

* Fri Nov 13 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.10-1.R
- update to 0.9.10

* Tue Oct 27 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.6-1.R
- clean up spec
- update to 0.9.6

* Mon Aug 03 2015 rommon <rommon@t-online.de> - 0.8.45-1
- update to new version

* Sat Jul 18 2015 rommon <rommon@t-online.de> - 0.8.38-1
- update to new version

* Fri Jun 26 2015 rommon <rommon@t-online.de> - 0.8.32-1
- update to new version
- rename from telegram to telegram-desktop

* Tue Jun 9 2015 rommon <rommon@t-online.de> - 0.8.24-1
- update to new version

* Fri May 1 2015 rommon <rommon@t-online.de> - 0.8.11-1
- update to new version

* Mon Apr 27 2015 rommon <rommon@t-online.de> - 0.8.7-1
- update to new version

* Mon Apr 27 2015 rommon <rommon@t-online.de> - 0.8.4-5
- fix icon permissions

* Fri Apr 24 2015 rommon <rommon@t-online.de> - 0.8.4-4
- fix desktop file

* Tue Apr 21 2015 rommon <rommon@t-online.de> - 0.8.4-3
- changed desktop file

* Tue Apr 21 2015 rommon <rommon@t-online.de> - 0.8.4-2
- adaption for 32/64 bit builds

* Tue Apr 21 2015 rommon <rommon@t-online.de> - 0.8.4-1
- initial package