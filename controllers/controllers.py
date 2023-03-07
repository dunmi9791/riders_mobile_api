# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from datetime import datetime
from datetime import date , time, timedelta
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta


class MobileApiSamples(http.Controller):
    @http.route('/samples/', website=True, type='json', cors='*', auth='user')
    def samplesall(self):
        # return "List of all Samples"
        samples_list = []
        samples_all = request.env['sample.transport'].search([])
        for rec in samples_all:
            vals = {
                'id': rec.id,
                'name': rec.st_no,
                'specimen_type': rec.specimen_type,
                'total_samples': rec.total_samples_sent,
                'temperature_at_send': rec.temperature_send,
                'sending_facility': rec.sending_lab.name,

            }
            samples_list.append(vals)

        data = {'status': 200, 'response': samples_list, 'message': 'Samples Returned'}
        return data


class MobileApiSamplesDetails(http.Controller):
    @http.route('/samples/details', website=True, type='json', cors='*', auth='user')
    def samplesall(self, sample):
        # return "List of all Samples"
        samples_list = []
        sample = request.params.get('sample')

        domain = [('id', '=', sample)]
        samples_all = request.env['sample.transport'].search(domain)

        for rec in samples_all:
            vals = {
                'id': rec.id,
                'name': rec.st_no,
                'specimen_type': rec.specimen_type,
                'total_samples': rec.total_samples_sent,
                'temperature_at_send': rec.temperature_send,
                'sending_facility': rec.sending_lab.name,
                'receiving_lab': rec.receiving_lab.name,
                'receiving_staff': rec.receiving_staff.name,
                'temperature_receive': rec.temperature_receive,
                'receive_time': rec.date_time_received,
                'patient_codes': rec.patient_sample_details,
                'sent_time': rec.date_time_sent,
                'test_type': rec.test_type,
                '3pl_name': rec.third_pl.name,
                '3pl_phone': rec.third_pl.phone,

            }
            samples_list.append(vals)

        data = {'status': 200, 'response': samples_list, 'message': 'Samples Returned'}
        return data


class MobileApiSample(http.Controller):
    @http.route('/samples/id/', website=True, type='json', cors='*', auth='user')
    def samplesall(self):
        # return "List of all Samples"
        samples_list = []
        samples_all = request.env['sample.transport'].search([])
        for rec in samples_all:
            vals = {
                'id': rec.id,
                'name': rec.st_no,
                'specimen_type': rec.specimen_type,
                'total_samples': rec.total_samples_sent,
                'temperature_at_send': rec.temperature_send,
                'sending_facility': rec.sending_lab,

            }
            samples_list.append(vals)

        data = {'status': 200, 'response': samples_list, 'message': 'Samples Returned'}
        return data


class MobileApiResults(http.Controller):
    @http.route('/results/', website=True, type='json', cors='*', auth='user')
    def resultsall(self):
        # return "List of all Samples"
        results_list = []
        results_all = request.env['result.transport'].search([])
        for rec in results_all:
            vals = {
                'id': rec.id,
                'name': rec.rt_no,
                'test_type': rec.test_type,
                'total_results': rec.total_results_sent,

            }
            results_list.append(vals)

        data = {'status': 200, 'response': results_list, 'message': 'Results Returned'}
        return data


class MobileApiResultsDetails(http.Controller):
    @http.route('/results/details', website=True, type='json', cors='*', auth='user')
    def resultsall(self, result):
        # return "List of all Samples"
        results_list = []
        result = request.params.get('sample')

        domain = [('id', '=', result)]
        results_all = request.env['result.transport'].search(domain)

        for rec in results_all:
            vals = {
                'id': rec.id,
                'name': rec.st_no,
                'specimen_type': rec.specimen_type,
                'total_samples': rec.total_samples_sent,
                'temperature_at_send': rec.temperature_send,
                'sending_facility': rec.sending_lab.name,
                'receiving_lab': rec.receiving_lab.name,
                'receiving_staff': rec.receiving_staff.name,
                'temperature_receive': rec.temperature_receive,
                'receive_time': rec.date_time_received,
                'patient_codes': rec.patient_result_details,
                'sent_time': rec.date_time_sent,
                'test_type': rec.test_type,
                '3pl_name': rec.third_pl.name,
                '3pl_phone': rec.third_pl.phone,

            }
            results_list.append(vals)

        data = {'status': 200, 'response': results_list, 'message': 'Results Returned'}
        return data


class MobileApiSampleCount(http.Controller):
    @http.route('/samples/count/', website=True, type='json', cors='*', auth='user')
    def samplescount(self):
        # return "Count of all Samples"

        samples_count = request.env['sample.transport'].search_count([])

        data = {'status': 200, 'response': samples_count, 'message': 'Samples  Count Returned'}
        return data


class MobileApiResultCount(http.Controller):
    @http.route('/results/count', website=True, type='json', cors='*', auth='user')
    def resultscount(self):
        # return "Count of all Samples"

        results_count = request.env['result.transport'].search_count([])

        data = {'status': 200, 'response': results_count, 'message': 'Results Count Returned'}
        return data


class MobileApiTestTypes(http.Controller):
    @http.route('/testtypes/', website=True, type='json', cors='*', auth='public')
    def testtypes(self):
        # return "List of all Samples"
        tests_list = []
        tests_all = request.env['test.type'].search([])
        for rec in tests_all:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            tests_list.append(vals)

        data = {'status': 200, 'response': tests_list, 'message': 'Test Types Returned'}
        return data


class MobileApiFacility(http.Controller):
    @http.route('/facilities/', website=True, type='json', cors='*', auth='public')
    def facilitiesall(self):
        # return "List of all Samples"
        facilities_list = []
        facilities_all = request.env['lab.facility'].search([])
        for rec in facilities_all:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            facilities_list.append(vals)

        data = {'status': 200, 'response': facilities_list, 'message': 'Facilities Returned'}
        return data


class MobileApiPatients(http.Controller):
    @http.route('/patients/', website=True, type='json', cors='*', auth='public')
    def patientsall(self):
        # return "List of all Samples"
        patients_list = []
        patients_all = request.env['patient.code'].search([])
        for rec in patients_all:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            patients_list.append(vals)

        data = {'status': 200, 'response': patients_list, 'message': 'Facilities Returned'}
        return data


class MobileFacilityStaff(http.Controller):
    @http.route('/facilitystaffs/', website=True, type='json', cors='*', auth='public')
    def facilitystaffall(self):
        # return "List of all Samples"
        facilitystaffs_list = []
        facilitystaffs_all = request.env['staff.facility'].search([])
        for rec in facilitystaffs_all:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            facilitystaffs_list.append(vals)

        data = {'status': 200, 'response': facilitystaffs_list, 'message': 'Facility Staffs Returned'}
        return data


class Mobile3pl(http.Controller):
    @http.route('/3pl/', website=True, type='json', cors='*', auth='public')
    def plall(self):
        # return "List of all Samples"
        thirdpl_list = []
        thirdpl_all = request.env['third.pl'].search([])
        for rec in thirdpl_all:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'phone': rec.phone,

            }
            thirdpl_list.append(vals)

        data = {'status': 200, 'response': thirdpl_list, 'message': 'Third PL  Returned'}
        return data


class TestType(http.Controller):
    @http.route('/testtype/', website=True, type='json', cors='*', auth='public')
    def testtype(self):
        # return "List of all Samples"
        test_list = []
        test_all = request.env['test.type'].search([])
        for rec in test_all:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            test_list.append(vals)

        data = {'status': 200, 'response': test_list, 'message': 'Test Type  Returned'}
        return data


class NewAuth(http.Controller):
    @http.route('/web/session/auth', type='json', cors='*', auth="none")
    def auth(self, db, login, password, base_location=None):
        request.session.authenticate(db, login, password)
        return request.env['ir.http'].session_info()
# class RidersMobileApi(http.Controller):
#     @http.route('/riders_mobile_api/riders_mobile_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/riders_mobile_api/riders_mobile_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('riders_mobile_api.listing', {
#             'root': '/riders_mobile_api/riders_mobile_api',
#             'objects': http.request.env['riders_mobile_api.riders_mobile_api'].search([]),
#         })

#     @http.route('/riders_mobile_api/riders_mobile_api/objects/<model("riders_mobile_api.riders_mobile_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('riders_mobile_api.object', {
#             'object': obj
#         })