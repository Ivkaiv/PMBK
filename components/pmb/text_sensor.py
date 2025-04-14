import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID

pmb_ns = cg.esphome_ns.namespace('pmb')
PMBTextSensor = pmb_ns.class_('PMBTextSensor', text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(PMBTextSensor),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield text_sensor.register_text_sensor(var, config)