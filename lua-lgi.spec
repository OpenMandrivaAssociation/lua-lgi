%define lua_version 5.1

Summary:        Dynamic Lua binding to GObject libraries using GObject-Introspection
Name:           lua-lgi
Version:        0.6.2
Release:        3
License:        MIT
Group:          Development/Other
URL:            http://www.tecgraf.puc-rio.br/~diego/professional/luasocket/
Source0:        lgi-%{version}.tar.gz
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
LGI is gobject-introspection based dynamic Lua binding to GObject based
libraries. It allows using GObject-based libraries directly from Lua.

%prep
%setup -q -n lgi-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
%make

%install
%makeinstall_std LUA_SHAREDIR=%{_datadir}/lua/%{lua_version} LUA_LIBDIR=%{_libdir}/lua/%{lua_version}

%files
%doc docs/
%doc README.md
%{_datadir}/lua/%{lua_version}/lgi*
%{_libdir}/lua/%{lua_version}/lgi
