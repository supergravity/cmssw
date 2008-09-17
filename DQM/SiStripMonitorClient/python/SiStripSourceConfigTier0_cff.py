import FWCore.ParameterSet.Config as cms

# SiStripMonitorTrack ####
from DQM.SiStripMonitorTrack.SiStripMonitorTrack_cfi import *
SiStripMonitorTrack.TrackProducer = 'generalTracks'
SiStripMonitorTrack.Mod_On        = False
SiStripMonitorTrack.FolderName    = 'SiStrip/Tracks'

# TrackerMonitorTrack ####
from DQM.TrackerMonitorTrack.MonitorTrackResiduals_cfi import *
MonitorTrackResiduals.trajectoryInput = 'generalTracks'
MonitorTrackResiduals.OutputMEsInRootFile = False
MonitorTrackResiduals.Mod_On = False

# TrackingMonitor ####
from DQM.TrackingMonitor.TrackingMonitor_cfi import *
TrackMon.TrackProducer = 'generalTracks'
TrackMon.AlgoName = 'GenTk'
TrackMon.FolderName = 'SiStrip/Tracks'

# Sequence
SiStripDQMTier0 = cms.Sequence(SiStripMonitorTrack*MonitorTrackResiduals*TrackMon)


