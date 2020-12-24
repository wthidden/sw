;;;
;;; Star web
;;;
(ql:quickload "alexandria")
(ql:quickload "vecto")
(defpackage #:sw
  (:use #:flexi-streams #:clim-lisp #:clim #:cl #:vecto :alexandria))
;; Good practice
(in-package #:sw)

(defstruct player
  (name nil)
  (allies nil)                          ;a sequence of players
  (at-war nil)                          ;a sequence of players
  (assets nil)                          ;a sequence of fleets/keys and worlds
  )

(defvar world-states '(:normal :at-war :plundered :gifted :threatened))

(defstruct world
  (owner nil)
  (name nil)
  (connections nil)
  (state nil)
  (population 0)
  (population-limit 0)
  (converts 0)
  (robots 0)
  (industry 0)
  (mines 0)
  (iships 0)
  (pships 0)
  (metal 0)
  (artifacts nil)
  )

(defstruct fleet
  (owner nil)
  (name nil)
  (state nil)
  (fleets 0)
  (cargo 0)
  (pbb 0)
  (artifacts nil)
  )

(defun update-world (w)
  (if (< (world-population w) (world-population-limit w))
      (setf (world-population w) (1+ (world-population w)))
      (world-population w)))
  
(defun do-turn (stream players worlds fleets)
  (let ((commands (read-player-commands stream)))
    
    (process-builds commands)
    (process-moves commands)
    (process-fire commands)
    (update-worlds)
    (update-fleets)
    (update-score))
  )
