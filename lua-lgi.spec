%define lua_version 5.1
%define _disable_lto 1

Summary:	Dynamic Lua binding to GObject libraries using GObject-Introspection
Name:		lua-lgi
Version:	0.9.2
Release:	1
License:	MIT
Group:		Development/Other
Url:		http://www.tecgraf.puc-rio.br/~diego/professional/luasocket/
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
LGI is gobject-introspection based dynamic Lua binding to GObject based
libraries. It allows using GObject-based libraries directly from Lua.

%files
%doc docs/
%doc README.md
%{_datadir}/lua/%{lua_version}/lgi*
%{_libdir}/lua/%{lua_version}/lgi

#----------------------------------------------------------------------------

%prep
%setup -q -n lgi-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
%make_build

%install
%make_install LUA_SHAREDIR=%{_datadir}/lua/%{lua_version} LUA_LIBDIR=%{_libdir}/lua/%{lua_version}
