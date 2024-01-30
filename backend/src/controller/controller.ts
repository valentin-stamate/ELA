import { Request, Response, NextFunction } from "express";
import { ESOLangService } from "../service/esolang.service";
import { ESOLangFilter } from "../interface/interface";

export class Controller {

  static async getCategories(req: Request<any>, res: Response, next: NextFunction): Promise<any> {

    try {
      const data = await ESOLangService.getCategories();

      res.setHeader('Content-type', 'application/json');
      res.end(JSON.stringify(data));
    } catch (err) {
      next(err);
    }

  }

  static async getWithFilter(req: Request<any>, res: Response, next: NextFunction): Promise<any> {

    const filter: ESOLangFilter = req.query;

    try {
      const data = await ESOLangService.getWithFilter(filter);

      res.setHeader('Content-type', 'application/json');
      res.end(JSON.stringify(data));
    } catch (err) {
      next(err);
    }

  }

  static async getRecommendation(req: Request<any>, res: Response, next: NextFunction): Promise<any> {

    const preferences: string[] = (req.query.preference as string).split(',');

    try {
      const data = await ESOLangService.getRecommendation(preferences);

      res.setHeader('Content-type', 'application/json');
      res.end(JSON.stringify(data));
    } catch (err) {
      next(err);
    }

  }

}
