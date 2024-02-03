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

  static async getData(key: string, body: any = null) {
    return await axios.post(`${BackendService.HOST}/api/get-data/`,body, {
      params: {
        key: key,
      }
    });
  }

}
