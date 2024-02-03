import axios from "axios";

export class BackendService {

  static HOST = 'http://localhost:8000'

  static async getSpecificData(esolang: string) {
    return await axios.get(`${BackendService.HOST}/api/get-specific-data`, {
      params: {
        key: 'esolang_data',
        value: esolang.split('#')[1]
      },
    });
  }

  static async getData() {
    return await axios.get(`${BackendService.HOST}/api/get-data`, {
      params: {
        key: 'esolangs_labels',
      },
    });
  }

}
