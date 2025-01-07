%global debug_package %{nil}
%define lua_version 5.4
%define _disable_lto 1

Summary:	Dynamic Lua binding to GObject libraries using GObject-Introspection
Name:		lua-lgi
Version:	0.9.2
Release:	3
License:	MIT
Group:		Development/Other
Url:		https://www.tecgraf.puc-rio.br/~diego/professional/luasocket/
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(libffi)

%patchlist
https://github.com/lgi-devs/lgi/commit/5cfd42c386d3adae6d211fbb4011179c3c141b04.patch

%description
LGI is gobject-introspection based dynamic Lua binding to GObject based
libraries. It allows using GObject-based libraries directly from Lua.

%prep
%autosetup -p1 -n lgi-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
%make_build

%install
%make_install LUA_SHAREDIR=%{_datadir}/lua/%{lua_version} LUA_LIBDIR=%{_libdir}/lua/%{lua_version}

%files
%doc README.md docs/*
%{_libdir}/lua/%{lua_version}/lgi/corelgilua51.so
%{_datadir}/lua/%{lua_version}/lgi*
