;; Auto-generated. Do not edit!


(when (boundp 'functionplotter::valuepair)
  (if (not (find-package "FUNCTIONPLOTTER"))
    (make-package "FUNCTIONPLOTTER"))
  (shadow 'valuepair (find-package "FUNCTIONPLOTTER")))
(unless (find-package "FUNCTIONPLOTTER::VALUEPAIR")
  (make-package "FUNCTIONPLOTTER::VALUEPAIR"))

(in-package "ROS")
;;//! \htmlinclude valuepair.msg.html


(defclass functionplotter::valuepair
  :super ros::object
  :slots (_t _h ))

(defmethod functionplotter::valuepair
  (:init
   (&key
    ((:t __t) 0.0)
    ((:h __h) 0.0)
    )
   (send-super :init)
   (setq _t (float __t))
   (setq _h (float __h))
   self)
  (:t
   (&optional __t)
   (if __t (setq _t __t)) _t)
  (:h
   (&optional __h)
   (if __h (setq _h __h)) _h)
  (:serialization-length
   ()
   (+
    ;; float32 _t
    4
    ;; float32 _h
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _t
       (sys::poke _t (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _h
       (sys::poke _h (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _t
     (setq _t (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _h
     (setq _h (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get functionplotter::valuepair :md5sum-) "771d8d2e2ad1eb8d6a85efe6f09ba042")
(setf (get functionplotter::valuepair :datatype-) "functionplotter/valuepair")
(setf (get functionplotter::valuepair :definition-)
      "float32 t
float32 h

")



(provide :functionplotter/valuepair "771d8d2e2ad1eb8d6a85efe6f09ba042")


