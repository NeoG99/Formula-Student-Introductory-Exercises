// Generated by gencpp from file functionplotter/valuepair.msg
// DO NOT EDIT!


#ifndef FUNCTIONPLOTTER_MESSAGE_VALUEPAIR_H
#define FUNCTIONPLOTTER_MESSAGE_VALUEPAIR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace functionplotter
{
template <class ContainerAllocator>
struct valuepair_
{
  typedef valuepair_<ContainerAllocator> Type;

  valuepair_()
    : t(0.0)
    , h(0.0)  {
    }
  valuepair_(const ContainerAllocator& _alloc)
    : t(0.0)
    , h(0.0)  {
  (void)_alloc;
    }



   typedef float _t_type;
  _t_type t;

   typedef float _h_type;
  _h_type h;





  typedef boost::shared_ptr< ::functionplotter::valuepair_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::functionplotter::valuepair_<ContainerAllocator> const> ConstPtr;

}; // struct valuepair_

typedef ::functionplotter::valuepair_<std::allocator<void> > valuepair;

typedef boost::shared_ptr< ::functionplotter::valuepair > valuepairPtr;
typedef boost::shared_ptr< ::functionplotter::valuepair const> valuepairConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::functionplotter::valuepair_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::functionplotter::valuepair_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::functionplotter::valuepair_<ContainerAllocator1> & lhs, const ::functionplotter::valuepair_<ContainerAllocator2> & rhs)
{
  return lhs.t == rhs.t &&
    lhs.h == rhs.h;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::functionplotter::valuepair_<ContainerAllocator1> & lhs, const ::functionplotter::valuepair_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace functionplotter

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::functionplotter::valuepair_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::functionplotter::valuepair_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::functionplotter::valuepair_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::functionplotter::valuepair_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::functionplotter::valuepair_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::functionplotter::valuepair_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::functionplotter::valuepair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "771d8d2e2ad1eb8d6a85efe6f09ba042";
  }

  static const char* value(const ::functionplotter::valuepair_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x771d8d2e2ad1eb8dULL;
  static const uint64_t static_value2 = 0x6a85efe6f09ba042ULL;
};

template<class ContainerAllocator>
struct DataType< ::functionplotter::valuepair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "functionplotter/valuepair";
  }

  static const char* value(const ::functionplotter::valuepair_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::functionplotter::valuepair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 t\n"
"float32 h\n"
;
  }

  static const char* value(const ::functionplotter::valuepair_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::functionplotter::valuepair_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.t);
      stream.next(m.h);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct valuepair_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::functionplotter::valuepair_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::functionplotter::valuepair_<ContainerAllocator>& v)
  {
    s << indent << "t: ";
    Printer<float>::stream(s, indent + "  ", v.t);
    s << indent << "h: ";
    Printer<float>::stream(s, indent + "  ", v.h);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FUNCTIONPLOTTER_MESSAGE_VALUEPAIR_H