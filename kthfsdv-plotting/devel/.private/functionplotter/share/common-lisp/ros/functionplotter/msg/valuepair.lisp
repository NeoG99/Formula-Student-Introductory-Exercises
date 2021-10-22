; Auto-generated. Do not edit!


(cl:in-package functionplotter-msg)


;//! \htmlinclude valuepair.msg.html

(cl:defclass <valuepair> (roslisp-msg-protocol:ros-message)
  ((t
    :reader t
    :initarg :t
    :type cl:float
    :initform 0.0)
   (h
    :reader h
    :initarg :h
    :type cl:float
    :initform 0.0))
)

(cl:defclass valuepair (<valuepair>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <valuepair>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'valuepair)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name functionplotter-msg:<valuepair> is deprecated: use functionplotter-msg:valuepair instead.")))

(cl:ensure-generic-function 't-val :lambda-list '(m))
(cl:defmethod t-val ((m <valuepair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader functionplotter-msg:t-val is deprecated.  Use functionplotter-msg:t instead.")
  (t m))

(cl:ensure-generic-function 'h-val :lambda-list '(m))
(cl:defmethod h-val ((m <valuepair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader functionplotter-msg:h-val is deprecated.  Use functionplotter-msg:h instead.")
  (h m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <valuepair>) ostream)
  "Serializes a message object of type '<valuepair>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 't))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'h))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <valuepair>) istream)
  "Deserializes a message object of type '<valuepair>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 't) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'h) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<valuepair>)))
  "Returns string type for a message object of type '<valuepair>"
  "functionplotter/valuepair")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'valuepair)))
  "Returns string type for a message object of type 'valuepair"
  "functionplotter/valuepair")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<valuepair>)))
  "Returns md5sum for a message object of type '<valuepair>"
  "771d8d2e2ad1eb8d6a85efe6f09ba042")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'valuepair)))
  "Returns md5sum for a message object of type 'valuepair"
  "771d8d2e2ad1eb8d6a85efe6f09ba042")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<valuepair>)))
  "Returns full string definition for message of type '<valuepair>"
  (cl:format cl:nil "float32 t~%float32 h~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'valuepair)))
  "Returns full string definition for message of type 'valuepair"
  (cl:format cl:nil "float32 t~%float32 h~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <valuepair>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <valuepair>))
  "Converts a ROS message object to a list"
  (cl:list 'valuepair
    (cl:cons ':t (t msg))
    (cl:cons ':h (h msg))
))
