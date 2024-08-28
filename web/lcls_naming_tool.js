dy(function(){
    var fc_prefix = "";
    var fc_sequence_number = "";
    var fc_source_letter = "";
    var fc_beam_path = "";
    var fg_part_1 = "";
    var fg_part_2 = "";

    var pv_name = "";

    $('#fc_prefix').on('change', function() {
        fc_prefix = $(this).find('option:selected').data('value');
        pv_name += fc_prefix;
    });

    // pv_name += $('#fc_sequence_number').val()

    $('#fc_source_letter').on('change', function() {
        fc_source_letter = $(this).find('option:selected').data('value');
        pv_name += fc_source_letter;
    });

    $('#pv_name').text(pv_name);
  });


const fungible = {
    _4FCCM: '4-F Channel Cut Mono',
    _4FFOCUS: 'Mirror 4F Focus',
    ATM: 'Arrival time monitor',
    BCS: 'Beam containment stopper',
    BTM: 'Burn Thru Monitor',
    BEND: 'Bendable mirror, using piezo benders',
    C1: '',
    C2: '',
    CAT1: '',
    CAT2: '', 
    CATCH: '',  
    COIL: '', 
    CRYO: '', 
    DCCM: 'Double Channel Cut Mono', 
    DET: 'Detector?',
    DG3: 'Diagnostic Stand 3',
    DIA: 'Diagnostic Stand',
    DIAG: 'Diagnostics',
    DIFFRACT: 'Diffractometer',
    DIFFPUMP: 'Diffrenetial Pumping',
    DIODE: 'Diode',
    DP1: '',
    DP2: '',
    DP3: '',
    EXIT: 'Exit slits',
    FIM: 'Fluorescence Intensity Monitor',
    FLAT: '',
    GAS: 'Attenuator (as opposed to solid)',
    GAS_MA_X: 'Gas attenuator movable aperture x',
    GAS_MA_Y: 'Gas attenuator movable aperture y',
    GEM: 'Gas energy monitor',
    GJ: '',
    GJ1: '',
    GJ2: '',
    GMD: 'Gas monitor detector',
    GSJN: '',
    GSJP: '',
    HOMS: 'Hard-xray offset mirror system, using version I design from Axilon, circa 2017, revised in 2019',
    IP1: 'Interaction point 1',
    IPM: 'Intensity and Position Monitor',
    K2A: '',
    K2B: '',
    KBH: 'KBO optics (horizontal) (?)',
    KBO: 'Kirkpatrick-Baez optics',
    KBV: 'KBO optics (vertical) (?)',
    KMONO: 'K-line monochromator',
    L2SI: 'LCLS-2 Strategic Initiative Instruments',
    LAS: 'General laser prefix',
    LD1: 'Laser beam protection system - laser destination #1',
    LD10: 'Laser beam protection system - laser destination #n',
    LD14: 'Laser beam protection system - laser destination #n',
    LD2: 'Laser beam protection system - laser destination #n',
    LD4: 'Laser beam protection system - laser destination #n',
    LD6: 'Laser beam protection system - laser destination #n',
    LD8: 'Laser beam protection system - laser destination #n',
    LD9: 'Laser beam protection system - laser destination #n',
    LIC: 'Laser in-coupling mirrors',
    LOC: 'Laser out-coupling mirrors',
    LODCM: 'Large Offset Double Crystal Monochrometer. Also referred to as LOM (Large Offset Monochrometer)',
    LS1: 'Laser beam protection system - laser source #n',
    LS5: 'Laser beam protection system - laser source #n',
    LS8: 'Laser beam protection system - laser source #n',
    LUSI: 'LCLS Ultrafast Science Instruments',
    MAIN: '',
    MC: '',
    MECH: '',
    MONO: 'Monochromater',
    NC: '',
    PC1K4: '',  
    PICKER: 'Pulse picker',
    PLEG: '',
    POWER: 'Power slits',
    PPL: 'Patch panel',
    PPM: 'Power and Profile Monitor',
    PPS: 'Personel Protection System',
    PRE: 'Reflective Lens',
    REF: 'Referance Laser',
    RCC: '',
    RF_C: '',
    RF_E: '',
    RF_W: '',
    ROUGH: 'Roughing pump',
    ROUGH1: 'Roughing pump, again?',
    ROUGH2: 'Roughing pump, again again?',
    SC: '',
    SCATTER: 'Scatter slits',
    SDS: 'Sample Delivery System',
    SOLID_JJ: 'L2SI JJ-Xray Design (4 filters to an actuator) Attenuator',
    SOLID: 'Solid (attenuator, as oppsed to gas)',
    SOMS: 'Offset mirror system, using version I design from Axilon, circa 2017, revised in 2019',
    SSA: '',    
    SSL: '',
    SWITCH: 'Mirrors',
    TC: 'Thermocouple',
    TERM: 'Termination (stopper)',
    TEST: 'Test absorber (stopper)',
    TMO_TERM: '',
    TMO_TERM_FIXED: '', 
    TFCTR: 'Transfocator',
    TXI: 'TXI offset mirrors using mark II design from Axilon',
    UM6: 'A specific stand name in the XRT',
    VLS: '',
    WFS: 'Wavefront Sensor',
    XGMD: 'Gas monitor detector, enhanced version',
    XTES: '',
    YAGXRAY: '',    
    YAGXRAYB: '',
    ZOS: 'Zero order stopper',
};