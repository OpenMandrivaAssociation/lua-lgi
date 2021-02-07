%global debug_package %{nil}
%define lua_version 5.1
%define _disable_lto 1

Summary:	Dynamic Lua binding to GObject libraries using GObject-Introspection
Name:		lua-lgi
Version:	0.9.2
Release:	2
License:	MIT
Group:		Development/Other
Url:		http://www.tecgraf.puc-rio.br/~diego/professional/luasocket/
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
#BuildRequires:  pkgconfig(gmodule-2.0)
#BuildRequires:  pkgconfig(libffi)

%description
LGI is gobject-introspection based dynamic Lua binding to GObject based
libraries. It allows using GObject-based libraries directly from Lua.

%prep
%setup -q -n lgi-%{version}
%autopatch -p1

%build
%set_build_flags
export CFLAGS="%{optflags} -fPIC"
%make_build

%install
%make_install \
    PREFIX=%{_prefix} \
    LUA_LIBDIR=%{lualibdir} \
    LUA_SHAREDIR=%{luapkgdir}

%files
%doc README.md docs/*
%{lualibdir}/lgi/corelgilua52.so
%{luapkgdir}/lgi*
