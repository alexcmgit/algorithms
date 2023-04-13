<p><a href="https://www.beecrowd.com.br/repository/UOJ_2616_en.html">beecrowd.com.br/repository/UOJ_2616_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2616 </span>
                                    <h1>No Rental</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>The video store company intends to do a promotion for customers who have not yet done any rental.</p>
                                    <p>Your job is to deliver us the ID and the name of the customers who have not done any rental. Sort the output by ID.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>customers</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>street</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>city</td>
                                  <td>varchar</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>locations</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>locations_date</td>
                              <td>date (ISO/YMD)</td>
                            </tr>
                            <tr>
                              <td>id_customers (FK)</td>
                              <td>numeric</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>customers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Giovanna Goncalves Oliveira</td>
                      <td>Rua Mato Grosso</td>
                      <td>Canoas</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Kauã Azevedo Ribeiro</td>
                      <td>Travessa Ibiá</td>
                      <td>Uberlândia</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Rebeca Barbosa Santos</td>
                      <td>Rua Observatório Meteorológico</td>
                      <td>Salvador</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Sarah Carvalho Correia</td>
                      <td>Rua Antônio Carlos da Silva</td>
                      <td>Apucarana</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>João Almeida Lima</td>
                      <td>Rua Rio Taiuva</td>
                      <td>Ponta Grossa</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Diogo Melo Dias</td>
                      <td>Rua Duzentos e Cinqüenta</td>
                      <td>Várzea Grande</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>locations</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>locations_date</strong></td>
                  <td><strong>id_customers</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>2016-10-09</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>2016-09-02</td>
                  <td>1</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>2016-08-02</td>
                  <td>4</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>2016-09-02</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>2016-03-02</td>
                  <td>6</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>2016-04-04</td>
                  <td>4</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>id</strong></td>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>5</td>
          <td>João Almeida Lima</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>