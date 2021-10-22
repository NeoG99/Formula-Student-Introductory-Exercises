
(cl:in-package :asdf)

(defsystem "functionplotter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "valuepair" :depends-on ("_package_valuepair"))
    (:file "_package_valuepair" :depends-on ("_package"))
  ))